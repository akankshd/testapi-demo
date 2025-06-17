# FastAPI MongoDB Demo

A simple FastAPI application with MongoDB integration for learning purposes.

## Features

- 🚀 FastAPI web framework
- 🍃 MongoDB Atlas cloud database
- 📝 CRUD operations for catalog items
- 🔒 Environment-based configuration
- 📊 Interactive API documentation

## Setup Instructions

### 1. Clone and Setup Virtual Environment

```bash
git clone <your-repo-url>
cd fastapi-kanopy-demo
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Configuration

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your MongoDB credentials:
   ```
   MONGODB_USERNAME=your_mongodb_username
   MONGODB_PASSWORD=your_mongodb_password
   MONGODB_CLUSTER=your_cluster_url
   MONGODB_DATABASE=your_database_name
   ```

### 3. Initialize Database (Optional)

```bash
python setup_db.py
```

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

## API Endpoints

- `GET /` - Root endpoint
- `GET /docs` - Interactive API documentation
- `GET /catalog` - Get all catalog items
- `POST /catalog` - Add a new catalog item
- `GET /name` - Get name information
- `GET /name/details` - Get detailed name information

## Project Structure

```
fastapi-kanopy-demo/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── db.py                # Database connection
│   ├── models/
│   │   └── catalog.py       # Pydantic models
│   └── routes/
│       ├── __init__.py
│       ├── catalog.py       # Catalog endpoints
│       └── name.py          # Name endpoints
├── venv/                    # Virtual environment
├── .env                     # Environment variables (not in git)
├── .env.example             # Environment template
├── .gitignore              # Git ignore rules
├── requirements.txt        # Python dependencies
├── setup_db.py            # Database initialization script
└── README.md              # This file
```

## Security Notes

- Never commit `.env` files to version control
- Use strong passwords for your MongoDB cluster
- Restrict MongoDB network access to your IP addresses
- Consider using MongoDB connection string environment variables in production

## Technologies Used

- **FastAPI** - Modern Python web framework
- **MongoDB Atlas** - Cloud database service
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI server for FastAPI
- **Python-dotenv** - Environment variable management
