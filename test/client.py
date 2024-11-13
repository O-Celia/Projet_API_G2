import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import unittest
from fastapi.testclient import TestClient
from src.main import app

# @app.get("/")
# def home():
#     return {"message": "API démarrée"}


class TestHomeRoute(unittest.TestCase):
    def setUp(self):  # équivalent au __init__.py
        self.client = TestClient(app)

    def test_route_home(self):
        reponse = self.client.get("/")
        self.assertEqual(reponse.status_code, 200)  # reussite
        self.assertEqual(reponse.json(), {"message": "API démarrée"})  # bon le json


class TestGetClientRoute(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_route_get_client(self):
        reponse = self.client.get("/client")
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), list)
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
                self.assertIsInstance(clients, dict)
                self.assertEqual(set(clients.keys()), clés)
        else:
            self.assertEqual(reponse.json(), [])


class TestCreateClientRoute(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_route_create_client(self):
        client_data = {
            "prenomcli": "Test",
            "nomcli": "Client",
            "genrecli": "F",
        }
        reponse = self.client.post("/client", json=client_data)
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), dict)
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


class TestDeleteClientRoute(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

        reponse_ex = self.client.post(
            "/client/", json={"prenomcli": "Test", "nomcli": "Client", "genrecli": "M"}
        )
        self.client_id = reponse_ex.json().get("codcli")

    def test_route_delete_client(self):
        reponse = self.client.delete(f"/client/{self.client_id}")
        self.assertEqual(reponse.status_code, 200)
        self.assertIn(
            reponse.json().get("message"), ["Client supprimé", "Client n'existe pas"]
        )


class TestUpdateClientRoute(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

        reponse_ex = self.client.post(
            "/client/", json={"prenomcli": "Test", "nomcli": "Client", "genrecli": "M"}
        )
        self.client_id = reponse_ex.json().get("codcli")

    def test_route_update_client(self):
        update_data = {"prenomcli": "UpdateTest"}

        reponse_update = self.client.patch(
            f"/client/{self.client_id}", json=update_data
        )
        self.assertEqual(reponse_update.status_code, 200)
        self.assertIsInstance(reponse_update.json(), dict)

        if reponse_update.json().get("message"):
            self.assertEqual(
                reponse_update.json().get("message"), "Client n'existe pas"
            )
        else:
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


if __name__ == "__main__":
    unittest.main()
