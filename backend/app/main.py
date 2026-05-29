from fastapi import FastAPI
from app.api.routes import challan, laws, chat

app = FastAPI(title="DriveLegal API")

app.include_router(challan.router)
app.include_router(laws.router)
app.include_router(chat.router)

@app.get("/")
def home():
    return {"message": "DriveLegal Backend Running"}