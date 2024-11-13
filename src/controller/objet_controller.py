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
    maj_objet = db.query(Objet).filter(Objet.codobj == codobj).first()
    if not maj_objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    
    for key, value in objet.model_dump(exclude_unset=True).items():
        setattr(maj_objet, key, value)

    db.commit()
    db.refresh(maj_objet)
    return maj_objet


def delete_objet(codobj: int, db: Session):
    del_objet = db.query(Objet).filter(Objet.codobj == codobj).first()
    if not del_objet:
        raise HTTPException(status_code=404, detail="Objet non trouvé")
    
    db.delete(del_objet)
    db.commit()
    return del_objet