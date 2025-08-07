import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def call_gemini_api(prompt: str, use_json_schema: bool = False, schema: dict = None) -> str:
    try:
        api_key = os.getenv("API_KEY")
        
        # TEMPORARY DEBUGGING LINE
        print(f"--- Loaded API Key: {api_key} ---") 

        if not api_key:
            return "API Key not found. Please set the API_KEY environment variable."

        chat_history = [{"role": "user", "parts": [{"text": prompt}]}]
        payload = {"contents": chat_history}

        if use_json_schema and schema:
            payload["generationConfig"] = {
                "responseMimeType": "application/json",
                "responseSchema": schema
            }

        api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"

        response = requests.post(api_url, json=payload, timeout=30)

        if response.status_code == 200:
            result = response.json()
            if (result.get("candidates") and
                result["candidates"][0].get("content") and
                result["candidates"][0]["content"].get("parts")):
                return result["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return "Unexpected API response format."
        else:
            return f"API Error: {response.status_code} - {response.text}"

    except requests.exceptions.Timeout:
        return "⏱️ Request timed out. Please try again."
    except Exception as e:
        return f"Error calling Gemini API: {e}"
