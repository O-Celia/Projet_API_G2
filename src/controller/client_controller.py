from sqlalchemy.orm import Session

from src.models.models import Client
from src.database import SessionLocal


def get_clients(db: Session):
    return db.query(Client).all()