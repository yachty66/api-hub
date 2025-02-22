from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
import replicate
import os
from pydantic import BaseModel
import requests
import traceback
import logging
from dotenv import load_dotenv
from io import BytesIO
import base64
import boto3
import uuid

# Load environment variables
load_dotenv()

# Set up detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

def upload_to_s3(image_data: BytesIO, bucket_name: str) -> str:
    """
    Upload image data to S3 and return the URL
    """
    # Create S3 client
    s3_client = boto3.client('s3')
    
    # Generate unique filename with directory structure
    file_name = f"premium-ai-image-upscaler-api/{uuid.uuid4()}.png"
    
    # Upload the file
    image_data.seek(0)  # Reset file pointer to beginning
    s3_client.upload_fileobj(image_data, bucket_name, file_name)
    
    # Generate URL
    url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    return url


class ImageRequest(BaseModel):
    image_url: str
    prompt: str = None

@app.get("/upscale")
async def upscale_image(
    image_url: str,
    prompt: str
):
    try:
        token = os.getenv("REPLICATE_API_TOKEN")
        bucket_name = os.getenv("AWS_BUCKET_NAME")
        
        output = replicate.run(
            "batouresearch/magic-image-refiner:507ddf6f977a7e30e46c0daefd30de7d563c72322f9e4cf7cbac52ef0f667b13",
            input={
                "image": image_url,
                "prompt": prompt
            }
        )
        
        # Create a BytesIO object to store the image
        image_data = BytesIO()
        
        # Write the first output item directly to BytesIO
        for item in output:
            image_data.write(item.read())
            break
        
        # Upload to S3 and get URL
        s3_url = upload_to_s3(image_data, bucket_name)
        
        # Return JSON with S3 URL
        return {
            "status": "success",
            "url": s3_url
        }
            
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))