
""" 
Deploying a trained machine learning model as an inference endpoint in AWS SageMaker using Python involves several steps, assuming you have a trained model artifact (e.g., a .tar.gz file containing your model and any necessary inference scripts).
"""


'''Step 1:
 Import Libraries and Set up 
SageMaker Session:
============================'''
import sagemaker
from sagemaker.predictor import Predictor
from sagemaker.serializers import CSVSerializer # Or other appropriate serializer
from sagemaker.deserializers import CSVDeserializer # Or other appropriate deserializer

# Get the SageMaker session and execution role
sagemaker_session = sagemaker.Session()
role = sagemaker.get_execution_role()


'''Step 2: Create a SageMaker Model Object: 
=========================================='''
model_data_uri = "s3://your-s3-bucket/your-model-path/model.tar.gz" # Replace with your S3 URI
image_uri = sagemaker.image_uris.retrieve("xgboost", sagemaker_session.boto_region_name, "1.2-1") # Example for XGBoost

model = sagemaker.model.Model(
    image_uri=image_uri,
    model_data=model_data_uri,
    role=role,
    sagemaker_session=sagemaker_session
)


'''Step 3: Deploy the Model to an Endpoint:
=========================================='''
endpoint_name = "your-inference-endpoint-name" # Choose a unique name

predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.xlarge", # Choose an appropriate instance type
    endpoint_name=endpoint_name,
    serializer=CSVSerializer(), # Specify serializer for incoming data
    deserializer=CSVDeserializer() # Specify deserializer for outgoing predictions
)


'''Step 4: Invoke the Endpoint for Inference:
=============================================='''
import pandas as pd

# Example input data (replace with your actual data)
input_data = pd.DataFrame([[1, 2, 3, 4]])

# Make a prediction
prediction = predictor.predict(input_data.values)

print(f"Prediction: {prediction}")


'''Step 5: Clean Up (Optional but Recommended):
=============================================='''
predictor.delete_endpoint()


"""
Important Notes:----->
=======================
IAM Role:

inference.py:

Error Handling:

Cost Management:

"""
