from fastapi import FastAPI

# Chemin vers le dossier racine contenant `src`
from src.database import Base, engine
from src.router.client_router import router_client
from src.router.objet_router import router_objet
from src.models.models import Client, Commande, Detail, Objet, DetailObjet
from src.router.router_commandes import router_commande
from src.router.router_detail import router_detail

app = FastAPI()

Base.metadata.create_all(engine)

app = FastAPI(
    title="Intranet DIGICHEESE", description="Nouvelle API Digicheese", version="0.0.1"
)

app.include_router(router_client)
# Ajouter le routeur des objets
app.include_router(router_objet)
app.include_router(router_commande)
app.include_router(router_detail)


@app.get("/")
def home():
    return {"message": "API démarrée"}


@app.get("/client/commande/detail/")
def communes_clients():
    return {"Accès à la table Détail_Commande"}
