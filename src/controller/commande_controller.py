from sqlalchemy.orm import Session
from src.models.models import Commande
from src.schema.commande_schema import CommandeCreateSchema, CommandeUpdateSchema
from fastapi import HTTPException


def get_commande(db: Session):
    return db.query(Commande).all()


def create_commande(commande: CommandeCreateSchema, db: Session):
    db_commande = Commande(**commande.model_dump())
    db.add(db_commande)
    db.commit()
    db.refresh(db_commande)
    return db_commande


def update_commande(codcde: int, commande: CommandeUpdateSchema, db: Session):
    try:
        maj_commande = db.query(Commande).filter(Commande.codcde == codcde).first()
        for key, value in commande.model_dump(exclude_unset=True).items():
            setattr(maj_commande, key, value)
        db.commit()
        db.refresh(maj_commande)
        return maj_commande
    except:
        raise HTTPException(status_code=404, detail={"message": "Commande non trouvée"})


def delete_commande(codcde: int, db: Session):
    try:
        del_commande = db.query(Commande).filter(Commande.codcde == codcde).first()
        db.delete(del_commande)
        db.commit()
        return {"message": "Commande supprimée"}
    except:
        raise HTTPException(status_code=404, detail={"message": "Commande non trouvée"})
