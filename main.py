from fastapi import FastAPI
from app.chat import chat_with_model

app = FastAPI(title="AI Chatbot API")

@app.get("/")
def root():
    return {"status": "running", "message": "AI Chatbot API is live"}

@app.get("/chat/")
def chat(prompt: str):
    return {"response": chat_with_model(prompt)}
