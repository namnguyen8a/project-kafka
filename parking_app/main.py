
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import models
import uvicorn
import schemas
from database import SessionLocal, engine

import json
from kafka import KafkaProducer

KAFKA_TOPIC = "vehicles"

producer = KafkaProducer(bootstrap_servers="localhost:29092")

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/vehicles/")
def get_all_vehicles(db: Session = Depends(get_db)):
    db_all = db.query(models.Vehicle).all()
    #db_all_encode = [str(veh).encode('utf-8') for veh in db_all]
    #producer.send("vehicles", json.dumps(db_all_encode).encode("utf-8"))
    producer.send("vehicles", b'db_all')
    print(type(db_all))
    print(db_all)
    return db_all

@app.get("/vehicles/search")
def get_vehicles_by_name(vehicle: str, db: Session = Depends(get_db)):
    return db.query(models.Vehicle).filter(models.Vehicle.vehicle_name == vehicle).first()

@app.post("/vehicles/create")
def create_vehicle(veh: schemas.VehicleCreate, db: Session = Depends(get_db)):
    db_vehicles = models.Vehicle(vehicle_name=veh.vehicle_name,
                                vehicle_type=veh.vehicle_type, vehicle_fee=veh.vehicle_fee )
    db.add(db_vehicles)
    db.commit()
    db.refresh(db_vehicles)
    return db_vehicles


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)