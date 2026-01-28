import requests
from config import GEMINI_API_KEY

API = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def analyze(text):
    if not GEMINI_API_KEY:
        return "Gemini API key not set."

    payload = {
        "contents": [{
            "parts": [{
                "text": f"You are a senior bug bounty hunter. Analyze:\n{text}"
            }]
        }]
    }

    try:
        r = requests.post(f"{API}?key={GEMINI_API_KEY}", json=payload, timeout=20)
        return r.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"AI error: {e}"
