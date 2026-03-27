from fastapi import FastAPI
from app.chat import chat_with_model

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Chatbot API is running"}

@app.get("/chat/")
def chat(prompt: str):
    response = chat_with_model(prompt)
    return {"response": response}
