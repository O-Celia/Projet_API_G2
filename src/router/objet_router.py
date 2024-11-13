from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.schema.objet_schema import ObjetCreateSchema, ObjetUpdateSchema
from src.database import get_db
from src.controller import objet_controller as controller


router_objet = APIRouter(prefix="/objet", tags=["Objet"])


@router_objet.get("/", status_code=status.HTTP_200_OK)
def get_objets(db: Session = Depends(get_db)):
    return controller.get_objet(db)


@router_objet.post("/", status_code=status.HTTP_201_CREATED)
def create_objet(objet: ObjetCreateSchema, db: Session = Depends(get_db)):
    return controller.create_objet(objet, db)


@router_objet.patch("/{objet_id}", status_code=status.HTTP_200_OK)
def update_objet(codobj: int, objet: ObjetUpdateSchema, db: Session = Depends(get_db)):
    return controller.update_objet(codobj, objet, db)


@router_objet.delete("/{objet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_objet(codobj: int, db: Session = Depends(get_db)):
    return controller.delete_objet(codobj, db)
