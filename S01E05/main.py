import requests
from homework import Homework
import os
from dotenv import load_dotenv
from prompt import CENZURA
import json

load_dotenv()
API_KEY = os.getenv("API_KEY")
homework = Homework()


ulr = f"https://centrala.ag3nts.org/data/{API_KEY}/cenzura.txt"
model_url = "http://localhost:11434/api/generate"
homework_url = "https://centrala.ag3nts.org/report"

text = homework.get(ulr)
text = f"{CENZURA}: \n{text}"
payload = {"model": "gemma2:2b", "prompt": text, "stream": False}

response = requests.post(model_url, json=payload)
answer = json.loads(response.text)["response"]

answer_data = {"task": "CENZURA", "apikey": API_KEY, "answer": answer}

response = homework.post(url=homework_url, data=answer_data)
