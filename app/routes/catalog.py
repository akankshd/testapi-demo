from fastapi import APIRouter, HTTPException
from app.models.catalog import CatalogItem
from app.db import catalog_collection

router = APIRouter(prefix="/catalog", tags=["catalog"])

# Fallback in-memory storage if MongoDB is not available
fallback_catalog = [
    {"title": "Python 101"},
    {"title": "FastAPI for Beginners"}, 
    {"title": "MongoDB Integration (Fallback Mode)"}
]

@router.get("/") # GET to /catalog
def get_catalog():
    if catalog_collection is not None:
        # Use MongoDB
        items = list(catalog_collection.find({}, {"_id": 0}))  # Hide MongoDB internal _id
        return {"data": items, "source": "MongoDB"}
    else:
        # Use fallback in-memory storage
        return {"data": fallback_catalog, "source": "In-Memory (MongoDB unavailable)"}

@router.post("/") # POST method to /catalog 
def add_item(item: CatalogItem):
    new_item = item.dict()
    
    if catalog_collection is not None:
        # Use MongoDB
        try:
            catalog_collection.insert_one(new_item)
            return {"item": new_item, "source": "MongoDB", "status": "success"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    else:
        # Use fallback in-memory storage
        fallback_catalog.append(new_item)
        return {"item": new_item, "source": "In-Memory (MongoDB unavailable)", "status": "success"}

