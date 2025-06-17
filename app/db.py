from pymongo import MongoClient
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

try:
    # Get credentials from environment variables
    username = quote_plus(os.getenv("MONGODB_USERNAME", ""))
    password = quote_plus(os.getenv("MONGODB_PASSWORD", ""))
    cluster_url = os.getenv("MONGODB_CLUSTER", "")
    database_name = os.getenv("MONGODB_DATABASE", "kanopy_demo")
    
    if not all([username, password, cluster_url]):
        raise ValueError("Missing MongoDB credentials in environment variables")
    
    MONGO_URI = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"
    
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Test the connection
    client.admin.command('ping')
    
    db = client[database_name]
    catalog_collection = db["catalog"]
    print("✅ MongoDB connection successful!")

except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
    print("💡 Using in-memory storage as fallback")
    client = None
    db = None
    catalog_collection = None
