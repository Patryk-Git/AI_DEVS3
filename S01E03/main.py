import json
from homework import Homework
from model import Model
from prompts import CORRECT_MISTAKES
import os
from dotenv import load_dotenv

load_dotenv()

homework = Homework()
model = Model()
api_key = os.getenv("API_KEY")
print(api_key)
url = "https://centrala.ag3nts.org/report"

data = open("data.json", "r")
data_json = json.load(data)
test_data = data_json["test-data"]
chunk_size = len(test_data) // 100
print(f"Chunk size: {chunk_size}")


correct_data = []

for i in range(0, len(test_data), chunk_size):
    print(f"Chunk {(i // chunk_size) + 1}")
    chunk = test_data[i : i + chunk_size]
    response = model.chat(
        system_message=CORRECT_MISTAKES, user_message=json.dumps(chunk)
    )
    print(f"Response: {response}")
    correct_data.append(json.loads(response))
flattened_data = [item for sublist in correct_data for item in sublist]

data = {
    "apikey": f"{api_key}",
    "description": "This is simple calibration data used for testing purposes. Do not use it in production environment!",
    "copyright": "Copyright (C) 2238 by BanAN Technologies Inc.",
    "test-data": flattened_data,
}
answer_data = {"task": "JSON", "apikey": api_key, "answer": data}

print(answer_data)
response = homework.post(url=url, data=answer_data)
