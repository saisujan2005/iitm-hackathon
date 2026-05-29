from pydantic import BaseModel

class ChallanRequest(BaseModel):
    state: str
    violation: str
    vehicle_type: str
    repeat_offense: bool = False