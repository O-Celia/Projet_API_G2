from fastapi import FastAPI
# Chemin vers le dossier racine contenant `src`
from src.database import Base, engine
from src.router.router_client import router_client
from src.models.model import Client, Commande, Detail
from src.router.router_commandes import router_commande
from src.router.router_detail import router_detail
app = FastAPI()

Base.metadata.create_all(engine)

app = FastAPI(
    title="Intranet DIGICHEESE",
    description="Nouvelle API Digicheese",
    version="0.0.1"
)

app.include_router(router_client)
app.include_router(router_commande)
app.include_router(router_detail)

@app.get("/")
def home():
    return {"API démarrée"}


# @app.get("/client/")
# def clients():
#     return {"Accès à la table Client"}


# @app.get("/commande/")
# def adresses_clients():
#     return {"Accès à la table Commande"}


# @app.get("/detail/")
# def communes_clients():
#     return {"Accès à la table Détail_Commande"}
