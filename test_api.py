from google import genai
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

try:
    print("Loading API key...")
    api_key = os.getenv("GOOGLE_API_KEY")
    print("Key starts with:", api_key[:8])

    client = genai.Client(api_key=api_key)

    print("Calling Gemini...")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say hello"
    )

    print("SUCCESS!")
    print(response.text)

except Exception:
    traceback.print_exc()