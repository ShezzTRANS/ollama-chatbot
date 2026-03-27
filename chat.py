import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "qwen:0.5b")

def chat_with_model(prompt: str):
    # Mock response for Railway deployment
    return f"AI Response (demo): {prompt}"
