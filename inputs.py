from pydantic import BaseModel, Field
from typing import Optional

class FibonacciInput(BaseModel):
    n: int = Field(ge=0, description="n must be >= 0")

class FactorialInput(BaseModel):
    n: int = Field(ge=0, description="n must be >= 0")

class PowerInput(BaseModel):
    x: float
    y: float
