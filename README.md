# FastAPI MongoDB Demo

A simple FastAPI application with MongoDB integration, connecting the endpoint just for demo

Screenshots of the connection and the /catalog endpont
<img width="803" alt="Screenshot 2025-06-17 at 4 58 52 PM" src="https://github.com/user-attachments/assets/5f0515b3-00aa-4c46-b966-6d66a684f29f" />

<img width="517" alt="Screenshot 2025-06-17 at 4 59 02 PM" src="https://github.com/user-attachments/assets/d12a2517-da37-4d2b-8bf2-93a01759937e" />



## Setup Instructions

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
