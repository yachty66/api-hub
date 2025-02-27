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

## setup  

1. go to project page UI

2. Click the + create button at the top right

3. Choose "empty service"

4. Rename empty service to api and add all shared variables

5. set root directory to "apis/nameofservice"

5. Run "railway service" in CLI and choose the service we just created

6. Run "railway up" from root of directory

7. Service is connected now