import requests
from config import GEMINI_API_KEY

API = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def analyze(text):
    payload = {
        "contents": [{
            "parts": [{
                "text": f"""
You are a senior bug bounty hunter.
Analyze the following and suggest vulnerabilities and manual tests:

{text}
"""
            }]
        }]
    }

    r = requests.post(
        f"{API}?key={GEMINI_API_KEY}",
        json=payload,
        timeout=20
    )

    return r.json()["candidates"][0]["content"]["parts"][0]["text"]
