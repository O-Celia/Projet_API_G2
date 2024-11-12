from sqlalchemy.orm import Session

from src.models.models import Client, Commande, Detail
from src.database import SessionLocal
from src.schema.client_schema import ClientBaseSchema, ClientInDBSchema


def get_clients(db: Session):
    return db.query(Client).all()


def create_client(db: Session, client: ClientBaseSchema):
    new_client = Client(prenomcli=client.prenomcli, nomcli=client.nomcli)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    return new_client
