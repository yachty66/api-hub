## Start

1. make a copy of the folder "premium-ai-image-upscaler-api" and then rename the folder to the new api name

2. make a new logo size 360x360 

3. go to main and add the new code for the new model, next we want to test the code

## Railway setup

4. go to root directory and then do the following:

1. go to project page UI in railway

2. Click the + create button at the top right

3. Choose "empty service"

4. Rename empty service to api and add all shared variables

5. set root directory to "apis/nameofservice"

5. Run "railway service" in CLI and choose the service we just created

6. test new endpoint from previous created step by going to the directory from the api i wanna test and run:

railway run uvicorn main:app --reload

7. use python script to send request for example:

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

6. for deployment to prod go to root and run "railway up"

7. Service is connected now

1. start converting the openapi template to the new api endpoint we want to put on rapid

1. got to rapid api > studio > Add api project > name it like the folder > upload openapi file

2. make and add logo

3. Add before and after effect based on current model and paste those links in the respective sections of the docs as well

4. change rest of the docs (todo make this section better)

3. put following prompt together with description in claude: 

"""
I have a api with the following docs:

---
docs
---

I need a short and long description for rapid api - make both extremely short!
"""

and use the result on rapid.

4. deploy the api endpoint

5. click test endpoint in rapid and see if we get result

6. create the webpage in the frontend for the api