from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.schema.client_schema import (
    ClientBaseSchema,
    ClientUpdateSchema,
    ClientCreateSchema,
)
from src.database import get_db
from src.controller import client_controller as controller


router_client = APIRouter(prefix="/client", tags=["Client"])


@router_client.get("/")
def get_clients(db: Session = Depends(get_db)):
    return controller.get_clients(db)


@router_client.post("/")
def create_client(client: ClientCreateSchema, db: Session = Depends(get_db)):
    return controller.create_client(client, db)


@router_client.delete("/{client_id}")
def delete_client(client_id, db: Session = Depends(get_db)):
    return controller.delete_client(client_id, db)


@router_client.patch("/{client_id}")
def update_client(client_id, client: ClientUpdateSchema, db: Session = Depends(get_db)):
    return controller.update_client(client_id, client, db)
