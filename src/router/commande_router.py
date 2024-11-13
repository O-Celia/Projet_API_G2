from fastapi import APIRouter,  Depends, HTTPException
from sqlalchemy.orm import Session
from src.controller import commande_controller
from src.schema.commande_schema import CommandeCreateSchema, CommandeInDBSchema
from src.database import get_db
from typing import List
from src.database import get_db
from src.controller import commande_controller as controller
from src.schema.commande_schema import CommandeBaseSchema, CommandeInDBSchema

router_commande = APIRouter(prefix='/commande', tags=["Commande"])

@router_commande.get('/') #, response_model=CommandeInDBSchema
def get_detail(db: Session = Depends(get_db)):
    return controller.get_detail(db)

@router_commande.post('/') #, response_model=CommandeInDBSchema, status_code=201
def create_commande(commande: CommandeCreateSchema, db: Session = Depends(get_db)):
    return controller.create_commande(commande, db)

