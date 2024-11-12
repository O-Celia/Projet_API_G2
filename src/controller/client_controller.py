from sqlalchemy.orm import Session
from src.schema.client_schema import ClientCreateSchema
from src.models.models import Client


def get_clients(db: Session):
    return db.query(Client).all()

def create_client(client: ClientCreateSchema, db: Session):
    # Transforme le schema en modèle SQLAlchemy
    new_client = Client(**client.model_dump())  # **client.model_dump() pour mettre le client en dict au cas où ça ne passe pas    
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def update_client():
    pass

def delete_client():
    pass