from app.db import catalog_collection

# Add some initial data to MongoDB
initial_data = [
    {"title": "Python 101"},
    {"title": "FastAPI for Beginners"},
    {"title": "MongoDB Test"},
    {"title": "Second day as a MongoDB Intern"},
]

# Clear existing data and insert initial data (optional)
catalog_collection.delete_many({})  # Clear collection
catalog_collection.insert_many(initial_data)

print(f"Inserted {len(initial_data)} items into MongoDB catalog collection")
print("Initial data setup complete!")
