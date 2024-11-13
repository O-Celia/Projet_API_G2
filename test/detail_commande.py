import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import unittest
from fastapi.testclient import TestClient
from main import app
from typing import List, Dict
import time
from sqlalchemy.orm import Session


class TestDetailCommandeRoute(unittest.TestCase):
    def setUp(self):  # équivalent au __init__.py
        self.detail_commande = TestClient(app)

    def test_route_home(self):
        reponse = self.detail_commande.get("/")
        self.assertEqual(reponse.status_code, 200)  # reussite
        self.assertEqual(reponse.json(), {"message": "API démarrée"})  # bon le json

    def test_route_get_detail_commande(self):
        reponse = self.detail_commande.get("/detail")
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), List)
        clés = {
            "commentaire",
            "codcde",
            "qte",
            "colis",
            "id",
        }

        if reponse.json():
            for details in reponse.json():
                self.assertIsInstance(details, Dict)
                self.assertEqual(set(details.keys()), clés)
        else:
            self.assertEqual(reponse.json(), [])

    def test_time_get_detail_commande(self):
        start_time = time.time()
        self.detail_commande.get("/detail")
        end_time = time.time()
        self.assertTrue(end_time - start_time < 1)

    def test_route_create_detail_commande(self):
        detailC_data = {
            "codcde": 2,
            "qte": 1,
            "colis": 1,
        }
        reponse = self.detail_commande.post("/detail", json=detailC_data)
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), Dict)
        clés = {
            "commentaire",
            "codcde",
            "qte",
            "colis",
            "id",
        }
        self.assertTrue(clés.issubset(reponse.json().keys()))
        self.detail_commande.delete(f"/detail/{reponse.json()['id']}")

    def test_charge_create_detail_commande(self):
        nombre_detailC_avant = len(self.detail_commande.get("/detail").json())
        for _ in range(1000):
            self.detail_commande.post(
                "/detail",
                json={"codcde": 2, "qte": 1, "colis": 1},
            )
        reponse_total = self.detail_commande.get("/detail")
        self.assertEqual(reponse_total.status_code, 200)
        nombre_detailC_apres = len(reponse_total.json())
        detailsC_ajoutes = nombre_detailC_apres - nombre_detailC_avant
        self.assertEqual(detailsC_ajoutes, 1000)

        details = reponse_total.json()
        for detailC in details:
            if detailC["codcde"] == 2 and detailC["colis"] == 1:
                self.detail_commande.delete(f"/detail/{detailC['id']}")

    def test_route_delete_detail_commande(self):

        reponse_ex = self.detail_commande.post(
            "/detail/", json={"codcde": 2, "qte": 1, "colis": 1}
        )
        self.detailC_id = reponse_ex.json().get("id")

        reponse = self.detail_commande.delete(f"/detail/{self.detailC_id}")
        self.assertEqual(reponse.status_code, 200)

    def test_delete_detail_not_found(self):
        invalid_detailC_id = 9999999
        reponse = self.detail_commande.delete(f"/detail/{invalid_detailC_id}")
        self.assertEqual(reponse.status_code, 404)

    def test_route_update_detail_commande(self):
        reponse_ex = self.detail_commande.post(
            "/detail/", json={"codcde": 2, "qte": 1, "colis": 1}
        )
        self.detailC_id = reponse_ex.json().get("id")

        update_data = {"codcde": 12}

        reponse_update = self.detail_commande.patch(
            f"/detail/{self.detailC_id}", json=update_data
        )
        self.assertEqual(reponse_update.status_code, 200)
        self.assertIsInstance(reponse_update.json(), Dict)

        clés = {
            "commentaire",
            "codcde",
            "qte",
            "colis",
            "id",
        }
        self.assertTrue(clés.issubset(reponse_update.json().keys()))
        self.assertEqual(reponse_update.json().get("codcde"), 12)
        self.detail_commande.delete(f"/detail/{reponse_update.json()['id']}")

    def test_update_detail_commande_not_found(self):
        invalid_detailC_id = 999999
        update_data = {"codcde": 8}
        reponse_update = self.detail_commande.patch(
            f"/detail/{invalid_detailC_id}", json=update_data
        )
        self.assertEqual(reponse_update.status_code, 404)


if __name__ == "__main__":
    unittest.main()
