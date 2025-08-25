
"""Deploying a trained 
machine learning model for 
inference in AWS SageMaker and 
cleaning up the associated resources 
involves several steps using the 
SageMaker Python SDK"""


'''Step 1:Deploying the Model: '''
============================
import sagemaker
from sagemaker.predictor import Predictor

# Initialize SageMaker session
sagemaker_session = sagemaker.Session()

# Define model data S3 path (replace with your actual path)
model_data_s3_path = 's3://your-bucket/your-model-artifacts/model.tar.gz'

# Define the SageMaker estimator or framework (e.g., PyTorch, TensorFlow, Scikit-learn)
# This example uses a PyTorch model
from sagemaker.pytorch import PyTorchModel

model = PyTorchModel(
    model_data=model_data_s3_path,
    role=sagemaker.get_execution_role(),
    framework_version='1.9.0', # Specify your framework version
    py_version='py38', # Specify your Python version
    entry_point='inference.py' # Your inference script
)

# Deploy the model to an endpoint
instance_type = 'ml.m5.large'
initial_instance_count = 1
endpoint_name = 'my-inference-endpoint' # Choose a unique name

predictor = model.deploy(
    instance_type=instance_type,
    initial_instance_count=initial_instance_count,
    endpoint_name=endpoint_name
)

print(f"Model deployed to endpoint: {endpoint_name}")


'''Step 2: Performing Inference: '''
=============================
# Example inference (replace with your actual input data)
input_data = [1, 2, 3, 4] # Example input for your model
prediction = predictor.predict(input_data)
print(f"Inference result: {prediction}")


'''Step 3: Cleaning Up Resources: '''
=============================
# Delete the endpoint
predictor.delete_endpoint()
print(f"Endpoint '{endpoint_name}' deleted.")

# Optionally, if you also created a model object that is no longer needed, delete it
# This is usually not necessary if the model data is in S3 and you only deployed an endpoint
# model.delete_model()
# print("Model deleted (if applicable).")

"""
Important Notes:----->
=======================
IAM Role:

inference.py:

Error Handling:

Cost Management:

"""
