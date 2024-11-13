from fastapi import FastAPI
from src.database import Base, engine
from src.router.client_router import router_client
from src.router.objet_router import router_objet

app = FastAPI(
    title="Intranet DIGICHEESE",
    description="Nouvelle API Digicheese",
    version="0.0.1"
)
# Ajouter le routeur du client
app.include_router(router_client)
# Ajouter le routeur des objets
app.include_router(router_objet)

Base.metadata.create_all(engine)

@app.get("/")
def home():
    return {"API démarrée"}


