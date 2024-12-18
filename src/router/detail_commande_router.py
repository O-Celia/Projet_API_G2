from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.database import get_db
from src.controller import detail_commande_controller as controller
from src.schema.detail_commande_schema import (
    DetailBaseSchema,
    DetailInDBSchema,
    DetailUpdateSchema,
    DetailCreateSchema,
)

router_detail = APIRouter(prefix="/commande/detail", tags=["Details commande"])


@router_detail.get("/")
def get_detail(db: Session = Depends(get_db)):
    return controller.get_details(db)


@router_detail.post("/")
def create_detail(detail: DetailCreateSchema, db: Session = Depends(get_db)):
    return controller.create_detail(detail, db)


@router_detail.patch("/{id}")
def update_detail(id: int, detail: DetailUpdateSchema, db: Session = Depends(get_db)):
    return controller.update_detail(id, detail, db)


@router_detail.delete("/{id}")
def delete_detail(id: int, db: Session = Depends(get_db)):
    return controller.delete_detail(id, db)
