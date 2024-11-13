from sqlalchemy.orm import Session
from src.models.model import Commande
from src.schema.commande_schema import CommandeCreateSchema

def get_commandes(db: Session):
    return db.query(Commande).all()

def create_commande(commande: CommandeCreateSchema, db: Session):
    db_commande = Commande(**commande.model_dump())
    db.add(db_commande)
    db.commit()
    db.refresh(db_commande)
    return db_commande

def update_commande():
    pass

def delete_commande():
    pass
