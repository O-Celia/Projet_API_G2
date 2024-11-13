from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.schema.objet_schema import ObjetCreateSchema, ObjetUpdateSchema
from src.database import get_db
from src.controller import objet_controller as controller


router_objet = APIRouter(prefix='/objet', tags=["Objet"])


@router_objet.get('/')
def get_objets(db: Session = Depends(get_db)):
    return controller.get_objet(db)

@router_objet.post('/')
def create_objet(objet: ObjetCreateSchema, db: Session = Depends(get_db)):
    return controller.create_objet(objet, db)

@router_objet.put("/{codobj}")
def update_objet(codobj: int, objet: ObjetUpdateSchema, db: Session = Depends(get_db)):
    return controller.update_objet(codobj, objet, db)

@router_objet.delete('/{codobj}')
def delete_objet(codobj: int, db: Session = Depends(get_db)):
    return controller.delete_objet(codobj, db)
