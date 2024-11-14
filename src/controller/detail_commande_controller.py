from sqlalchemy.orm import Session
from src.models.models import Detail
from src.schema.detail_commande_schema import DetailCreateSchema, DetailUpdateSchema
from fastapi import HTTPException


def get_details(db: Session):
    return db.query(Detail).all()


def create_detail(detail: DetailCreateSchema, db: Session):
    new_detail = Detail(**detail.model_dump())
    db.add(new_detail)
    db.commit()
    db.refresh(new_detail)
    return new_detail


def update_detail(id: int, detail: DetailUpdateSchema, db: Session):
    try:
        maj_detail = db.query(Detail).filter(Detail.id == id).first()
        for key, value in detail.model_dump(exclude_unset=True).items():
            setattr(maj_detail, key, value)
        db.commit()
        db.refresh(maj_detail)
        return maj_detail
    except:
        raise HTTPException(status_code=404, detail={"message": "Détail non trouvé"})


def delete_detail(id: int, db: Session):
    try:
        del_detail = db.query(Detail).filter(Detail.id == id).first()
        db.delete(del_detail)
        db.commit()
        return del_detail
    except:
        raise HTTPException(status_code=404, detail={"message": "Détail non trouvé"})
