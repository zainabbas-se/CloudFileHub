import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def get_s3_client():
    try:
        return boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION")
        )
    except Exception as e:
        print("S3 Client Error:", e)
        return None


def test_s3_connection():
    try:
        s3 = get_s3_client()
        s3.list_buckets()
        return True
    except Exception as e:
        print("S3 Connection Error:", e)
        return False


def upload_to_s3(file, expire_seconds=3600):
    """Upload a file and return a pre-signed URL valid for expire_seconds."""
    try:
        s3 = get_s3_client()
        bucket = os.getenv("AWS_BUCKET_NAME")

        if not bucket:
            raise ValueError("Bucket name not found in environment variables")

        file.seek(0)

        s3.upload_fileobj(
            Fileobj=file,
            Bucket=bucket,
            Key=file.name,
            ExtraArgs={'ContentType': file.type}
        )

        # Generate pre-signed URL
        file_url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': bucket, 'Key': file.name},
            ExpiresIn=expire_seconds
        )

        return file_url

    except Exception as e:
        print("Upload error:", e)
        return None
