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

# Load environment variables
load_dotenv()

# Set up detailed logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

class ImageRequest(BaseModel):
    image_url: str
    prompt: str = None

@app.post("/upscale")
async def upscale_image(request: ImageRequest):
    try:
        # Get token and validate
        token = os.getenv("REPLICATE_API_TOKEN")
        if not token:
            logger.error("No Replicate API token found")
            raise HTTPException(
                status_code=500, 
                detail="Replicate API token not configured"
            )
        
        logger.info("Token found and validated")
        
        # Run the model exactly as shown in the example
        output = replicate.run(
            "batouresearch/magic-image-refiner:507ddf6f977a7e30e46c0daefd30de7d563c72322f9e4cf7cbac52ef0f667b13",
            input={
                "image": request.image_url,
                "prompt": request.prompt
            }
        )
        
        # Create a BytesIO object to store the image
        image_data = BytesIO()
        
        # Write the first output item directly to BytesIO
        for item in output:
            image_data.write(item.read())
            break  # We only need the first image
            
        # Reset the BytesIO position to the beginning
        image_data.seek(0)
            
        return Response(
            content=image_data.getvalue(),
            media_type="image/png",
            headers={
                "Content-Disposition": "attachment; filename=upscaled_image.png"
            }
        )
            
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(status_code=500, detail=str(e))