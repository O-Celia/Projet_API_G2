from sqlalchemy.orm import Session
from src.models.model import Detail
from src.schema.detail_schema import DetailCreateSchema

def get_details(db: Session):
    return db.query(Detail).all()

def create_detail(detail: DetailCreateSchema, db: Session): 
        new_detail = detail(**detail.model_dump())  
        db.add(new_detail)
        db.commit()
        db.refresh(new_detail)
        return new_detail

def update_detail():
    pass

def delete_detail():
    pass
