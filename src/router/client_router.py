from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.schema.client_schema import ClientBaseSchema, ClientInDBSchema
from src.database import get_db
from src.controller import client_controller as controller


router_client = APIRouter(prefix="/client", tags=["Client"])


@router_client.get("/", response_model=ClientInDBSchema)
def get_clients(db: Session = Depends(get_db)):
    return controller.get_clients(db)


@router_client.post("/", response_model=ClientInDBSchema)
def create_client(client: ClientBaseSchema, db: Session = Depends(get_db)):
    return controller.create_client(db, client)
