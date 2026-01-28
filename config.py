import os

VERSION = "1.2.0"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("Set GEMINI_API_KEY environment variable")
