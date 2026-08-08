from fastapi import FastAPI
from pydantic import BaseModel
from main import ask_chatbot

app = FastAPI(
    title ="Simple ChatBot API",
    vesrion = "1.0"
)

class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

@app.get("/")
def home():
    return {
        "message": "Chatbot API is running"
    }

@app.post("/chat",response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = ask_chatbot(request.question)
    return ChatResponse(answer=answer)

# Entry point
if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )