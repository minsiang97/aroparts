from app import app
import boto3, botocore


s3 = boto3.client(
   "s3",
   aws_access_key_id=app.config.get("S3_KEY"),
   aws_secret_access_key=app.config.get("S3_SECRET")
)
