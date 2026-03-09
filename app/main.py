from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import routes
from app.database import Base, engine
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FitBuddy - AI Fitness Plan Generator")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

app.include_router(routes.router)
