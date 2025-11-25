#!/bin/sh
echo "---------------------------------------------"
echo "FastAPI server is starting!"
echo "Check the API docs at: http://localhost:8000/docs"
echo "---------------------------------------------"

# Start FastAPI
uvicorn app.main:app --host 0.0.0.0 --port 8000