from fastapi import APIRouter
from app.models.catalog import CatalogItem

router = APIRouter(prefix="/catalog", tags=["catalog"])

fake_catalog = [
    {"id": 1, "title": "Python 101"},
    {"id": 2, "title": "FastAPI for Beginners"},
    {"id": 3, "title": "Day Two @ MongoDB"},
    {"id": 4, "title": "Learning FastAPI"},
    {"id": 5, "title": "Random Message here"}
]

@router.get("/") # GET to /catalog
def get_catalog():
    return fake_catalog

@router.post("/") # POST method to /catalog 
def add_item(item: CatalogItem):
    new_item = item.dict()
    new_item["id"] = len(fake_catalog) + 1
    fake_catalog.append(new_item)
    return new_item

