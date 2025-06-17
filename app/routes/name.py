from fastapi import APIRouter

router = APIRouter(prefix="/name", tags=["name"])

@router.get("/")
def get_name():
    return {
        "name": "Akanksh Suhas Divyananda Kondajji",
        "message": "Test! name endpoint is working"
    }

@router.get("/details")
def get_name_details():
    return {
        "first_name": "Akanksh",
        "middle_names": ["Suhas", "Divyananda"],
        "last_name": "Kondajji",
        "full_name": "Akanksh Suhas Divyananda Kondajji"
    }
