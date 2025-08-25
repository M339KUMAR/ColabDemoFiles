
import boto3
import sagemaker
from sagemaker.predictor import Predictor
from sagemaker.serializers import CSVSerializer
from sagemaker.deserializers import CSVDeserializer

# 1. Configuration
aws_region = 'your-aws-region'  # e.g., 'us-east-1'
sagemaker_role = 'arn:aws:iam::your-account-id:role/your-sagemaker-role'
s3_bucket = 'your-s3-bucket-name'
model_name = 'your-model-name'
endpoint_config_name = f'{model_name}-config'
endpoint_name = f'{model_name}-endpoint'
model_artifact_s3_path = f's3://{s3_bucket}/model_artifacts/model.tar.gz' # Path to your model artifacts in S3

# Initialize boto3 and SageMaker session
boto3_session = boto3.Session(region_name=aws_region)
sagemaker_session = sagemaker.Session(boto_session=boto3_session)
sm_client = boto3_session.client('sagemaker')

# 2. Create SageMaker Model
# Define the Docker image URI for your inference container (e.g., a pre-built SageMaker image or your custom ECR image)
# Example for a pre-built Scikit-learn image:
# image_uri = sagemaker.image_uris.retrieve(framework='sklearn', region=aws_region, version='0.23-1', py_version='py3')
# Replace with your actual image URI
image_uri = 'your-ecr-image-uri' # or use sagemaker.image_uris.retrieve for built-in algorithms

try:
    sm_client.create_model(
        ModelName=model_name,
        PrimaryContainer={
            'Image': image_uri,
            'ModelDataUrl': model_artifact_s3_path
        },
        ExecutionRoleArn=sagemaker_role
    )
    print(f"Model '{model_name}' created successfully.")
except sm_client.exceptions.ResourceAlreadyExists:
    print(f"Model '{model_name}' already exists.")

# 3. Create Endpoint Configuration
try:
    sm_client.create_endpoint_config(
        EndpointConfigName=endpoint_config_name,
        ProductionVariants=[
            {
                'VariantName': 'AllTraffic',
                'ModelName': model_name,
                'InitialInstanceCount': 1,
                'InstanceType': 'ml.t2.medium', # Choose an appropriate instance type
                'InitialVariantWeight': 1
            }
        ]
    )
    print(f"Endpoint configuration '{endpoint_config_name}' created successfully.")
except sm_client.exceptions.ResourceAlreadyExists:
    print(f"Endpoint configuration '{endpoint_config_name}' already exists.")

# 4. Deploy Model to Endpoint
try:
    sm_client.create_endpoint(
        EndpointName=endpoint_name,
        EndpointConfigName=endpoint_config_name
    )
    print(f"Endpoint '{endpoint_name}' creation initiated. Waiting for it to be InService...")
    
    # Wait for the endpoint to be in service
    waiter = sm_client.get_waiter('endpoint_in_service')
    waiter.wait(EndpointName=endpoint_name)
    print(f"Endpoint '{endpoint_name}' is InService.")

except sm_client.exceptions.ResourceAlreadyExists:
    print(f"Endpoint '{endpoint_name}' already exists.")

# 5. (Optional) Invoke the Endpoint for Inference
# This part is for demonstration and assumes your inference script handles CSV input/output
# predictor = Predictor(
#     endpoint_name=endpoint_name,
#     sagemaker_session=sagemaker_session,
#     serializer=CSVSerializer(),
#     deserializer=CSVDeserializer()
# )
#
# sample_data = [[1.0, 2.0, 3.0, 4.0]] # Replace with your actual sample data
# prediction = predictor.predict(sample_data)
# print(f"Prediction: {prediction}")

# 6. (Optional) Clean up resources (uncomment to run)
# sm_client.delete_endpoint(EndpointName=endpoint_name)
# sm_client.delete_endpoint_config(EndpointConfigName=endpoint_config_name)
# sm_client.delete_model(ModelName=model_name)
