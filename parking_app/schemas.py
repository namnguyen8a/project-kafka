from pydantic import BaseModel

class VehicleCreate(BaseModel):
    vehicle_name: str
    vehicle_type: str
    vehicle_fee: int
