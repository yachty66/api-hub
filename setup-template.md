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