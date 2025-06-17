from fastapi import FastAPI
from app.routes import catalog
from app.routes import name
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title=os.getenv("API_TITLE", "FastAPI MongoDB Demo"),
    description=os.getenv("API_DESCRIPTION", "A demo API with MongoDB integration"),
    version=os.getenv("API_VERSION", "1.0.0")
)

@app.get("/") # HTTP GET request to root URL
def read_root():
    return {"message": "Root", "docs": "/docs"}

app.include_router(catalog.router)
app.include_router(name.router)


