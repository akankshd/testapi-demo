from fastapi import FastAPI
from app.routes import catalog
from app.routes import name

app = FastAPI(title="Kanopy Demo API", description="A simple catalog API", version="1.0.0")

@app.get("/") # HTTP GET request to root URL
def read_root():
    return {"message": "Root", "docs": "/docs"}

app.include_router(catalog.router)
app.include_router(name.router)


