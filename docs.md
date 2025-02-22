## Test locally with runway

1. go to directory of api you wanna test and run:

railway run uvicorn main:app --reload

2. use python script to send request for example:

import requests

# Test the API
response = requests.get(
    "http://127.0.0.1:8000/upscale",
    params={
        "image_url": "https://storage.googleapis.com/apihub85/0_1.webp",  # use a real image URL
        "prompt": "UHD 4k vogue style"
    }
)

print(response.json())

3. 