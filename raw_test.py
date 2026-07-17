import os
import requests
from dotenv import load_dotenv

print("Starting script...")

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print("API key:", repr(api_key))

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Say hello"
                }
            ]
        }
    ]
}

print("Sending request...")

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print(response.text)