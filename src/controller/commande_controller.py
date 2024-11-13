from sqlalchemy.orm import Session
from src.models.model import Commande
from src.schema.commande_schema import CommandeCreateSchema, CommandeUpdateSchema
from fastapi import HTTPException

def get_commandes(db: Session):
    return db.query(Commande).all()

def create_commande(commande: CommandeCreateSchema, db: Session):
    db_commande = Commande(**commande.model_dump())
    db.add(db_commande)
    db.commit()
    db.refresh(db_commande)
    return db_commande

def update_commande(codcde: int, commande: CommandeUpdateSchema, db: Session):
    maj_commande= db.query(Commande).filter(Commande.codcde == codcde).first()
    if not maj_commande:
        raise HTTPException(status_code=404, detail="commande non trouvé")
    
    for key, value in commande.model_dump(exclude_unset=True).items():
        setattr(maj_commande, key, value)

    db.commit()
    db.refresh(maj_commande)
    return maj_commande


def delete_commande(codcde: int, db: Session):
    del_commande = db.query(Commande).filter(Commande.codcde == codcde).first()
    if not del_commande:
        raise HTTPException(status_code=404, detail="Commande non trouvé")
    
    db.delete(del_commande)
    db.commit()
    return del_commande
