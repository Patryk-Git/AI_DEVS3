from homework import *
from prompts import USER_MESSAGE
from model import *
import os
from dotenv import load_dotenv
import json

# Load environment variables from a .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
homework = Homework()
model = Model()

data = {"text": "READY", "msgID": "0"}
url = "https://xyz.ag3nts.org/verify"
init_message = homework.post(data=data, url=url)
print(f"Init message: {init_message}")
data_dict = json.loads(init_message)
msg_id = data_dict["msgID"]
answer = model.chat(system_message=init_message, user_message=USER_MESSAGE)
print(f"Answer: {answer}")
data = {"text": answer, "msgID": msg_id}
response = homework.post(data=data, url=url)
print(response)
