from app.core.s3 import s3_client
from app.core.config import config

def upload_to_storage(img_bytes: bytes, filename: str) -> str:
    s3_client.put_object(
        Bucket=config.S3_BUCKET_NAME,
        Key=filename,
        Body=img_bytes,
        ContentType="image/png",
    )

    public_base_url = config.S3_BACE_URL
    
    return f"{public_base_url}/{config.S3_BUCKET_NAME}/{filename}"