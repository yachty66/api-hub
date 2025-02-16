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

# Load environment variables
load_dotenv()

# Set up detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

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
        if not token:
            raise HTTPException(
                status_code=500,
                detail="Replicate API token not configured"
            )
        
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
            
        # Convert to base64
        base64_image = base64.b64encode(image_data.getvalue()).decode('utf-8')
        
        # Return JSON with base64 image
        return {
            "status": "success",
            "image": base64_image,
            "format": "png"
        }
            
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))