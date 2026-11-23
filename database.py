import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def dbConnection():
    mongo_uri = os.getenv("MONGO_URI")

    if not mongo_uri:
        raise ValueError("No se encontró MONGO_URI en el archivo .env")

    client = MongoClient(mongo_uri, tlsCAFile=certifi.where())
    db = client["db_products_app"]

    return db