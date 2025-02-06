from fastapi import FastAPI
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_info():
    return {
        "email": os.getenv("REGISTERED_EMAIL"),
        "current_datetime": datetime.now(pytz.utc).isoformat(),
        "github_url": os.getenv("GITHUB_URL"),
    }
