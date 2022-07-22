from sqlalchemy import Column, Integer, String

from database import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_name = Column(String)
    #started_at = Column(Integer)
    #ended_at = Column(Integer)
    vehicle_fee = Column(Integer)
    vehicle_type = Column(String)

    class Vehicles_config:
        schema_extra = {
            "example": {
                "vehicle_name": "string",
                "vehicle_fee": "0",
                "vehicle_type": "string2"
            }
        }
