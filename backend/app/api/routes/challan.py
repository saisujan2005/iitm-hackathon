from fastapi import APIRouter
from app.schemas.challan_schema import ChallanRequest
from app.services.challan_service import calculate_fine

router = APIRouter(prefix="/challan", tags=["Challan"])

@router.post("/calculate")
def calculate(data: ChallanRequest):
    return calculate_fine(data)