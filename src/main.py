from fastapi import FastAPI
from src.database import Base, engine
from src.models.models import Client, Commande, Detail
from src.router.client_router import router_client

app = FastAPI()
app.include_router(router_client)

Base.metadata.create_all(engine)


@app.get("/")
def home():
    return {"API démarrée"}


@app.get("/client/")
def clients():
    return {"Accès à la table Client"}


@app.get("/client/commande/")
def commandes_clients():
    return {"Accès à la table Commande"}


@app.get("/client/commande/detail/")
def detail_commandes_clients():
    return {"Accès à la table Détail_Commande"}
