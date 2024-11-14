from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.schema.objet_schema import ObjetCreateSchema, ObjetUpdateSchema
from src.models.models import Objet


def get_objet(db: Session):
    return db.query(Objet).all()


def create_objet(objet: ObjetCreateSchema, db: Session):
    # Transforme le schema en modèle SQLAlchemy
    new_objet = Objet(**objet.model_dump())
    db.add(new_objet)
    db.commit()
    db.refresh(new_objet)
    return new_objet


def update_objet(codobj: int, objet: ObjetUpdateSchema, db: Session):
    try:
        maj_objet = db.query(Objet).filter(Objet.codobj == codobj).first()
        for key, value in objet.model_dump(exclude_unset=True).items():
            setattr(maj_objet, key, value)
        db.commit()
        db.refresh(maj_objet)
        return maj_objet
    except:
        raise HTTPException(status_code=404, detail="Objet non trouvé")


def delete_objet(codobj: int, db: Session):
    try:
        del_objet = db.query(Objet).filter(Objet.codobj == codobj).first()
        db.delete(del_objet)
        db.commit()
        return {"message": "Objet supprimé"}
    except:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
