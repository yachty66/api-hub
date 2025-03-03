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
import requests

# Load environment variables
load_dotenv()

# Set up detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

def upload_to_s3(image_data: BytesIO, bucket_name: str) -> str:
    """
    Upload file data to S3 and return the URL
    """
    # Create a session with AWS credentials
    session = boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    
    # Create S3 client using the session
    # s3_client = session.client('s3')
    
    # # Generate unique filename with directory structure
    # file_name = f"ai-3d-model-api/{uuid.uuid4()}.glb"
    
    # # Upload the file
    # file_data.seek(0)  # Reset file pointer to beginning
    # s3_client.upload_fileobj(file_data, bucket_name, file_name)
    
    # # Generate URL
    # url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
    return None

class ImageRequest(BaseModel):
    image_url: str
    prompt: str = None

@app.get("/3d")
async def generate_3d_model(
    image_url: str
):
    try:
        token = os.getenv("REPLICATE_API_TOKEN")
        bucket_name = os.getenv("AWS_BUCKET_NAME")
        
        print("before input")

        input={
            "seed": 0,
            "images": [image_url],
            "texture_size": 2048,
            "mesh_simplify": 0.9,
            "generate_color": True,
            "generate_model": True,
            "randomize_seed": True,
            "generate_normal": False,
            "save_gaussian_ply": True,
            "ss_sampling_steps": 38,
            "slat_sampling_steps": 12,
            "return_no_background": False,
            "ss_guidance_strength": 7.5,
            "slat_guidance_strength": 3
        }
        
        # Get the output from Replicate
        output = replicate.run(
            "firtoz/trellis:4876f2a8da1c544772dffa32e8889da4a1bab3a1f5c1937bfcfccb99ae347251",
            input=input
        )

        print("output is: ", output)
                    
        # Download the GLB file from Replicate
        response = requests.get(output['model_file'].url)
        file_data = BytesIO(response.content)
        
        # Upload to S3 and get URL
        s3_url = upload_to_s3(file_data, bucket_name)
        
        # Return JSON with S3 URL
        return {
            "status": "success",
            "url": s3_url
        }
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "status": "error",
            "message": "Error appeared please try again or reach out to support@apilexica.com"
        }