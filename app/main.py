from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import routes
from app.database import Base, engine
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FitBuddy - AI Fitness Plan Generator")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(BASE_DIR, "static")

if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(routes.router)
