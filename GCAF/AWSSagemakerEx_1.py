
#Step 1: Data Preperation & Upload to S3 
#=========================================

import sagemaker
from sagemaker.inputs import TrainingInput
import pandas as pd
from sklearn.model_selection import train_test_split

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()
bucket = sagemaker_session.default_bucket()
prefix = 'sagemaker-train-valid-test-example'

# Load your dataset (replace with your data loading method)
df = pd.read_csv('your_dataset.csv')

# Split data into train, validation, and test sets
train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)
validation_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

# Save datasets locally
train_df.to_csv('train.csv', index=False, header=False)
validation_df.to_csv('validation.csv', index=False, header=False)
test_df.to_csv('test.csv', index=False, header=False)

# Upload datasets to S3
train_s3_path = sagemaker_session.upload_data(path='train.csv', bucket=bucket, key_prefix=f'{prefix}/train')
validation_s3_path = sagemaker_session.upload_data(path='validation.csv', bucket=bucket, key_prefix=f'{prefix}/validation')
test_s3_path = sagemaker_session.upload_data(path='test.csv', bucket=bucket, key_prefix=f'{prefix}/test')

print(f"Train data uploaded to: {train_s3_path}")
print(f"Validation data uploaded to: {validation_s3_path}")
print(f"Test data uploaded to: {test_s3_path}") 

#Step 2: Create a Training Script: 
#======================================

# train.py
import argparse
import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--validation', type=str, default=os.environ.get('SM_CHANNEL_VALIDATION'))
    args = parser.parse_args()

    # Load training data
    train_data = pd.read_csv(os.path.join(args.train, 'train.csv'), header=None)
    X_train = train_data.iloc[:, :-1]
    y_train = train_data.iloc[:, -1]

    # Load validation data (for potential early stopping or hyperparameter tuning)
    validation_data = pd.read_csv(os.path.join(args.validation, 'validation.csv'), header=None)
    X_val = validation_data.iloc[:, :-1]
    y_val = validation_data.iloc[:, -1]

    # Train the model
    model = LogisticRegression(solver='liblinear')
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, os.path.join(args.model_dir, 'model.joblib')) 

#Step 3: Configure and Run SageMaker Training Job: 
#================================================== 

from sagemaker.sklearn.estimator import SKLearn

# Define the SageMaker role
role = sagemaker.get_execution_role()

# Create a SageMaker SKLearn Estimator
sklearn_estimator = SKLearn(
    entry_point='train.py',
    source_dir='.',  # Directory containing train.py and any other dependencies
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    framework_version='0.23-1', # Specify the Scikit-learn version
    hyperparameters={'epochs': 10} # Example hyperparameter
)

# Define training and validation data inputs
train_input = TrainingInput(train_s3_path, content_type='text/csv')
validation_input = TrainingInput(validation_s3_path, content_type='text/csv')

# Start the training job
sklearn_estimator.fit({'train': train_input, 'validation': validation_input}) 

#Step 4: Model Evaluation on Test Set (Post-Training): 
======================================================

import joblib
from sklearn.metrics import accuracy_score

# Download the trained model from S3
model_data_path = sklearn_estimator.model_data
sagemaker_session.download_data(path='.', bucket=bucket, key_prefix=f'{prefix}/output')

# Load the model
model = joblib.load('model.joblib')

# Load test data
test_data = pd.read_csv('test.csv', header=None)
X_test = test_data.iloc[:, :-1]
y_test = test_data.iloc[:, -1]

# Make predictions and evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Test Set Accuracy: {accuracy}")
