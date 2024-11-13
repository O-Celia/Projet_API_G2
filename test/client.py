import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import unittest
from fastapi.testclient import TestClient
from main import app
from typing import List, Dict

from sqlalchemy.orm import Session

# @app.get("/")
# def home():
#     return {"message": "API démarrée"}


class TestClientRoute(unittest.TestCase):
    def setUp(self):  # équivalent au __init__.py
        self.client = TestClient(app)

    def test_route_home(self):
        reponse = self.client.get("/")
        self.assertEqual(reponse.status_code, 200)  # reussite
        self.assertEqual(reponse.json(), {"message": "API démarrée"})  # bon le json

    def test_route_get_client(self):
        reponse = self.client.get("/client")
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), List)
        clés = {
            "codcli",
            "genrecli",
            "nomcli",
            "prenomcli",
            "adresse1cli",
            "adresse2cli",
            "adresse3cli",
            "telcli",
            "emailcli",
            "portcli",
            "newsletter",
        }

        if reponse.json():
            for clients in reponse.json():
                self.assertIsInstance(clients, Dict)
                self.assertEqual(set(clients.keys()), clés)
        else:
            self.assertEqual(reponse.json(), [])

    def test_route_create_client(self):
        client_data = {
            "prenomcli": "Test",
            "nomcli": "Client",
            "genrecli": "F",
        }
        reponse = self.client.post("/client", json=client_data)
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), Dict)
        clés = {
            "codcli",
            "genrecli",
            "nomcli",
            "prenomcli",
            "adresse1cli",
            "adresse2cli",
            "adresse3cli",
            "telcli",
            "emailcli",
            "portcli",
            "newsletter",
        }
        self.assertTrue(clés.issubset(reponse.json().keys()))
        self.client.delete(f"/client/{reponse.json()['codcli']}")

    def test_charge_create_client(self):
        nombre_clients_avant = len(self.client.get("/client").json())
        for _ in range(1000):
            self.client.post(
                "/client",
                json={"prenomcli": "Test", "nomcli": "Client", "genrecli": "M"},
            )
        reponse_total = self.client.get("/client")
        self.assertEqual(reponse_total.status_code, 200)
        nombre_clients_apres = len(reponse_total.json())
        clients_ajoutes = nombre_clients_apres - nombre_clients_avant
        self.assertEqual(clients_ajoutes, 1000)

        clients = reponse_total.json()
        for client in clients:
            if client["prenomcli"] == "Test" and client["nomcli"] == "Client":
                self.client.delete(f"/client/{client['codcli']}")

    def test_route_delete_client(self):

        reponse_ex = self.client.post(
            "/client/", json={"prenomcli": "Test", "nomcli": "Client", "genrecli": "M"}
        )
        self.client_id = reponse_ex.json().get("codcli")

        reponse = self.client.delete(f"/client/{self.client_id}")
        self.assertEqual(reponse.status_code, 200)

    def test_delete_client_not_found(self):
        invalid_client_id = 9999999
        reponse = self.client.delete(f"/client/{invalid_client_id}")
        self.assertEqual(reponse.status_code, 404)

    def test_route_update_client(self):
        reponse_ex = self.client.post(
            "/client/", json={"prenomcli": "Test", "nomcli": "Client", "genrecli": "M"}
        )
        self.client_id = reponse_ex.json().get("codcli")

        update_data = {"prenomcli": "UpdateTest"}

        reponse_update = self.client.patch(
            f"/client/{self.client_id}", json=update_data
        )
        self.assertEqual(reponse_update.status_code, 200)
        self.assertIsInstance(reponse_update.json(), Dict)

        clés = {
            "codcli",
            "genrecli",
            "nomcli",
            "prenomcli",
            "adresse1cli",
            "adresse2cli",
            "adresse3cli",
            "telcli",
            "emailcli",
            "portcli",
            "newsletter",
        }
        self.assertTrue(clés.issubset(reponse_update.json().keys()))
        self.assertEqual(reponse_update.json().get("prenomcli"), "UpdateTest")
        self.client.delete(f"/client/{reponse_update.json()['codcli']}")

    def test_update_client_not_found(self):
        invalid_client_id = 999999
        update_data = {"prenomcli": "UpdateTestFail"}
        reponse_update = self.client.patch(
            f"/client/{invalid_client_id}", json=update_data
        )
        self.assertEqual(reponse_update.status_code, 404)


if __name__ == "__main__":
    unittest.main()
