

from fastapi import FastAPI, HTTPException

from app.models import CalculationRequest, CalculationResponse

app = FastAPI(title="Calculator API", version="1.0.0")


@app.get("/health")
def health() -> dict:
    """Simple health check endpoint."""
    return {"status": "ok"}


@app.post("/add", response_model=CalculationResponse)
def add(payload: CalculationRequest) -> CalculationResponse:
    """Add two numbers."""
    result = payload.a + payload.b
    return CalculationResponse(result=result)


@app.post("/subtract", response_model=CalculationResponse)
def subtract(payload: CalculationRequest) -> CalculationResponse:
    """Subtract b from a."""
    result = payload.a - payload.b
    return CalculationResponse(result=result)


@app.post("/multiply", response_model=CalculationResponse)
def multiply(payload: CalculationRequest) -> CalculationResponse:
    """Multiply two numbers."""
    result = payload.a * payload.b
    return CalculationResponse(result=result)


@app.post("/divide", response_model=CalculationResponse)
def divide(payload: CalculationRequest) -> CalculationResponse:
    """Divide a by b, with simple zero-division protection."""
    if payload.b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero.")
    result = payload.a / payload.b
    return CalculationResponse(result=result)
