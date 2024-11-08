from fastapi import FastAPI
from src.database import Base, engine
from src.models.models import Client, Commande, Detail

app = FastAPI()

Base.metadata.create_all(engine)


@app.get("/")
def home():
    return {"API démarrée"}


@app.get("/client/")
def clients():
    return {"Accès à la table Client"}


@app.get("/client/commande/")
def adresses_clients():
    return {"Accès à la table Commande"}


@app.get("/client/commande/detail/")
def communes_clients():
    return {"Accès à la table Détail_Commande"}
