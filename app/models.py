from pydantic import BaseModel


class CalculationRequest(BaseModel):
    """Input payload for calculator operations."""
    a: float
    b: float


class CalculationResponse(BaseModel):
    """Standard response model for calculator results."""
    result: float

