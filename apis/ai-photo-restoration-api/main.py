from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
import replicate
import os
from pydantic import BaseModel
import logging
from dotenv import load_dotenv
from io import BytesIO
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
    # Create a session with AWS credentials
    session = boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    
    # Create S3 client using the session
    s3_client = session.client('s3')
    
    # Generate unique filename with directory structure
    file_name = f"ai-photo-restoration-api/{uuid.uuid4()}.png"
    
    # Upload the file
    image_data.seek(0)  # Reset file pointer to beginning
    s3_client.upload_fileobj(image_data, bucket_name, file_name)
    
    # Generate URL
    url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    return url


class ImageRequest(BaseModel):
    image_url: str
    prompt: str = None

@app.get("/restore")
async def upscale_image(
    image_url: str,
    prompt: str
):
    try:
        token = os.getenv("REPLICATE_API_TOKEN")
        bucket_name = os.getenv("AWS_BUCKET_NAME")

        input = {
            "jpeg": "40",
            "image": "https://api-lexica.s3.us-east-1.amazonaws.com/examples/dsc01290.jpg",
            "noise": "15"
        }
        
        output = replicate.run(
            "jingyunliang/swinir:660d922d33153019e8c263a3bba265de882e7f4f70396546b6c9c8f9d47a021a",
            input=input
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
        return {
            "status": "error",
            "message": "Error appeared please try again or reach out to support@apilexica.com"
        }
    

        