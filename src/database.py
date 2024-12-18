from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les variables
DB_USER = os.getenv("utilisateur")
DB_PASSWORD = os.getenv("password")
DB_HOST = os.getenv("host")
DB_NAME = os.getenv("bdd")
DB_CONNECTOR = os.getenv("connector")

# connexion a la base de donnée et déclaration de la base avec sql alchemy
# url de connexion de la base

# SQLALCHEMY_DATABASE_URL = (f"{DB_CONNECTOR}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")
SQLALCHEMY_DATABASE_URL = f"{DB_CONNECTOR}://{DB_USER}@{DB_HOST}/fromagerie_com"

# permet de définir les paramètre de connexion à la base
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# déclaration d'une base qui permet après de créer un modele et de mapper avec sql alchemy
Base = declarative_base()

# creation d'une session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    db = SessionLocal()
    try:
        yield db  # couplé avec Depends de fastapi
    finally:
        db.close()  # fermeture de la session
