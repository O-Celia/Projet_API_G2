import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import unittest
from fastapi.testclient import TestClient
from main import app
from typing import List, Dict
import time
from sqlalchemy.orm import Session


class TestCommandeRoute(unittest.TestCase):
    def setUp(self):  # équivalent au __init__.py
        self.commande = TestClient(app)

    def test_route_home(self):
        reponse = self.commande.get("/")
        self.assertEqual(reponse.status_code, 200)  # reussite
        self.assertEqual(reponse.json(), {"message": "API démarrée"})  # bon le json

    def test_route_get_commande(self):
        reponse = self.commande.get("/commande")
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), List)
        clés = {
            "codcli",
            "datcde",
            "nbcolis",
            "barchive",
            "bstock",
            "timbrecli",
            "timbrecde",
            "cheqcli",
            "cdeComt",
            "codcde",
        }

        if reponse.json():
            for commandes in reponse.json():
                self.assertIsInstance(commandes, Dict)
                self.assertEqual(set(commandes.keys()), clés)
        else:
            self.assertEqual(reponse.json(), [])

    def test_time_get_commande(self):
        start_time = time.time()
        self.commande.get("/commande")
        end_time = time.time()
        self.assertTrue(end_time - start_time < 1)

    def test_route_create_commande(self):
        commande_data = {"codcli": 999, "datcde": "2024-02-01"}
        reponse = self.commande.post("/commande", json=commande_data)
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), Dict)
        clés = {
            "codcli",
            "datcde",
            "nbcolis",
            "barchive",
            "bstock",
            "timbrecli",
            "timbrecde",
            "cheqcli",
            "cdeComt",
            "codcde",
        }
        self.assertTrue(clés.issubset(reponse.json().keys()))
        self.commande.delete(f"/commande/{reponse.json()['codcde']}")

    def test_charge_create_client(self):
        nombre_commandes_avant = len(self.commande.get("/commande").json())
        for _ in range(1000):
            self.commande.post(
                "/commande",
                json={"codcli": 999, "datcde": "2024-02-01"},
            )
        reponse_total = self.commande.get("/commande")
        self.assertEqual(reponse_total.status_code, 200)
        nombre_commandes_apres = len(reponse_total.json())
        commandes_ajoutes = nombre_commandes_apres - nombre_commandes_avant
        self.assertEqual(commandes_ajoutes, 1000)

        commandes = reponse_total.json()
        for commande in commandes:
            if commande["codcli"] == 999 and commande["datcde"] == "2024-02-01":
                self.commande.delete(f"/commande/{commande['codcde']}")

    def test_route_delete_commande(self):

        reponse_ex = self.commande.post(
            "/commande/",
            json={"codcli": 999, "datcde": "2024-02-01"},
        )
        self.commande_id = reponse_ex.json().get("codcde")

        reponse = self.commande.delete(f"/commande/{self.commande_id}")
        self.assertEqual(reponse.status_code, 200)

    def test_delete_commande_not_found(self):
        invalid_commande_id = 9999999
        reponse = self.commande.delete(f"/commande/{invalid_commande_id}")
        self.assertEqual(reponse.status_code, 404)

    def test_route_update_commande(self):
        reponse_ex = self.commande.post(
            "/commande/",
            json={"codcli": 999, "datcde": "2024-02-01"},
        )
        self.commande_id = reponse_ex.json().get("codcde")

        update_data = {"codcli": 1111}

        reponse_update = self.commande.patch(
            f"/commande/{self.commande_id}", json=update_data
        )
        self.assertEqual(reponse_update.status_code, 200)
        self.assertIsInstance(reponse_update.json(), Dict)

        clés = {
            "codcli",
            "datcde",
            "nbcolis",
            "barchive",
            "bstock",
            "timbrecli",
            "timbrecde",
            "cheqcli",
            "cdeComt",
            "codcde",
        }
        self.assertTrue(clés.issubset(reponse_update.json().keys()))
        self.assertEqual(reponse_update.json().get("codcli"), 1111)
        self.commande.delete(f"/commande/{reponse_update.json()['codcde']}")

    def test_update_commande_not_found(self):
        invalid_commande_id = 999999
        update_data = {"codcli": 444444}
        reponse_update = self.commande.patch(
            f"/commande/{invalid_commande_id}", json=update_data
        )
        self.assertEqual(reponse_update.status_code, 404)


if __name__ == "__main__":
    unittest.main()
