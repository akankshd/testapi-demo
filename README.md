# FastAPI MongoDB Demo

A simple FastAPI application with MongoDB integration for learning purposes.


## Setup Instructions

### 1. Clone and Setup Virtual Environment

```bash
git clone <your-repo-url>
cd fastapi-kanopy-demo
python -m venv venv
source venv/bin/activate  
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
