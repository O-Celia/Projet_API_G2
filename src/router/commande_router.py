from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.controller import commande_controller as controller
from src.schema.commande_schema import (
    CommandeCreateSchema,
    CommandeInDBSchema,
    CommandeUpdateSchema,
)
from src.database import get_db
from typing import List
from src.controller import commande_controller as controller


router_commande = APIRouter(prefix="/commande", tags=["Commande"])


@router_commande.get("/")
def get_commande(db: Session = Depends(get_db)):
    return controller.get_commande(db)


@router_commande.post("/")
def create_commande(commande: CommandeCreateSchema, db: Session = Depends(get_db)):
    return controller.create_commande(commande, db)


@router_commande.patch("/{codcde}")
def update_commande(
    codcde: int, commande: CommandeUpdateSchema, db: Session = Depends(get_db)
):
    return controller.update_commande(codcde, commande, db)


@router_commande.delete("/{codcde}")
def delete_commande(codcde: int, db: Session = Depends(get_db)):
    return controller.delete_commande(codcde, db)
