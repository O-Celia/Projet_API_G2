from sqlalchemy.orm import Session
from src.schema.client_schema import ClientCreateSchema, ClientUpdateSchema
from src.models.models import Client
from fastapi import HTTPException, status
from sqlalchemy.exc import NoResultFound

# from flask import Flask, jsonify


def get_clients(db: Session):
    return db.query(Client).all()


def create_client(client: ClientCreateSchema, db: Session):
    # Transforme le schema en modèle SQLAlchemy
    new_client = Client(
        **client.model_dump()
    )  # **client.model_dump() pour mettre le client en dict au cas où ça ne passe pas
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client


def update_client(client_id, client: ClientUpdateSchema, db: Session):
    try:
        updated = db.query(Client).filter(Client.codcli == client_id).one()
        for key, value in client.model_dump(exclude_unset=True).items():
            setattr(updated, key, value)
        db.commit()
        db.refresh(updated)
        return updated
    except:
        raise HTTPException(status_code=404, detail={"message": "Client n'existe pas"})


def delete_client(client_id: int, db: Session):
    try:
        client = db.query(Client).filter(Client.codcli == client_id).one()
        db.delete(client)
        db.commit()
        return {"message": "Client supprimé"}
    except:
        raise HTTPException(status_code=404, detail={"message": "Client n'existe pas"})
