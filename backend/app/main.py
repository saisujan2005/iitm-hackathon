from fastapi import FastAPI
from app.api.routes import challan, laws, chat, ocr
from app.db.database import Base, engine
from app.models.source import Source
from app.models.penalty import Penalty
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="DriveLegal API")

Base.metadata.create_all(bind=engine)

app.include_router(challan.router)
app.include_router(laws.router)
app.include_router(chat.router)

@app.get("/")
def home():
    return {"message": "DriveLegal Backend Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    ocr.router
)