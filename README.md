

React frontend
      |
      | HTTP GET /documents
      |
      v
FastAPI backend
      |
      | SQL query
      |
      v
PostgreSQL
      |
      | Documents
      |
      v
FastAPI → JSON response → React