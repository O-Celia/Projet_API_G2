from fastapi import FastAPI
from src.database import Base, engine
from src.models.models import Client, Commande, Detail

app = FastAPI()

Base.metadata.create_all(engine)


@app.get("/")
def home():
    return {}


@app.get("/client/")
def clients():
    return {}


@app.get("/client/commande/")
def adresses_clients():
    return {}


@app.get("/client/commande/detail/")
def communes_clients():
    return {}
