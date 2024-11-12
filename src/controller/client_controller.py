from sqlalchemy.orm import Session
from src.schema.client_schema import ClientCreateSchema
from src.models.models import Client


def get_clients(db: Session):
    return db.query(Client).all()

def create_client(client: ClientCreateSchema, db: Session):
    # Transforme le schema en modèle SQLAlchemy
    new_client = Client(genrecli=client.genrecli,
                        nomcli=client.nomcli,
                        prenomcli=client.prenomcli,
                        adresse1cli=client.adresse1cli,
                        adresse2cli=client.adresse2cli,
                        adresse3cli=client.adresse3cli,
                        telcli=client.telcli,
                        emailcli=client.emailcli,
                        portcli=client.portcli,
                        newsletter=client.newsletter)  # **client.model_dump() pour mettre le client en dict au cas où ça ne passe pas
    
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client