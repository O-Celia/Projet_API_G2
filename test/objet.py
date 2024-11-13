import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import unittest
from fastapi.testclient import TestClient
from main import app
from typing import List, Dict
import time
from sqlalchemy.orm import Session

# @app.get("/")
# def home():
#     return {"message": "API démarrée"}


class TestObjetRoute(unittest.TestCase):
    def setUp(self):  # équivalent au __init__.py
        self.objet = TestClient(app)

    def test_route_home(self):
        reponse = self.objet.get("/")
        self.assertEqual(reponse.status_code, 200)  # reussite
        self.assertEqual(reponse.json(), {"message": "API démarrée"})  # bon le json

    def test_route_get_objet(self):
        reponse = self.objet.get("/objet")
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), List)
        clés = {
            "libobj",
            "tailleobj",
            "puobj",
            "poidsobj",
            "indispobj",
            "o_imp",
            "o_aff",
            "o_cartp",
            "points",
            "o_ordre_aff",
            "codobj",
        }

        if reponse.json():
            for objets in reponse.json():
                self.assertIsInstance(objets, Dict)
                self.assertEqual(set(objets.keys()), clés)
        else:
            self.assertEqual(reponse.json(), [])

    def test_time_get_objet(self):
        start_time = time.time()
        self.objet.get("/objet")
        end_time = time.time()
        self.assertTrue(end_time - start_time < 1)

    def test_route_create_objet(self):
        objet_data = {
            "libobj": "ordi",
        }
        reponse = self.objet.post("/objet", json=objet_data)
        self.assertEqual(reponse.status_code, 200)
        self.assertIsInstance(reponse.json(), Dict)
        clés = {
            "libobj",
            "tailleobj",
            "puobj",
            "poidsobj",
            "indispobj",
            "o_imp",
            "o_aff",
            "o_cartp",
            "points",
            "o_ordre_aff",
            "codobj",
        }
        self.assertTrue(clés.issubset(reponse.json().keys()))
        self.objet.delete(f"/objet/{reponse.json()['codobj']}")

    def test_charge_create_objet(self):
        nombre_objets_avant = len(self.objet.get("/objet").json())
        for _ in range(1000):
            self.objet.post(
                "/objet",
                json={"libobj": "chargeur"},
            )
        reponse_total = self.objet.get("/objet")
        self.assertEqual(reponse_total.status_code, 200)
        nombre_objets_apres = len(reponse_total.json())
        objets_ajoutes = nombre_objets_apres - nombre_objets_avant
        self.assertEqual(objets_ajoutes, 1000)

        objets = reponse_total.json()
        for objet in objets:
            if objet["libobj"] == "chargeur":
                self.objet.delete(f"/objet/{objet['codobj']}")

    def test_route_delete_objet(self):

        reponse_ex = self.objet.post(
            "/objet/", json={"libobj": "souris", "tailleobj": 5}
        )
        self.objet_id = reponse_ex.json().get("codobj")

        reponse = self.objet.delete(f"/objet/{self.objet_id}")
        self.assertEqual(reponse.status_code, 200)

    def test_delete_objet_not_found(self):
        invalid_objet_id = 9999999
        reponse = self.objet.delete(f"/objet/{invalid_objet_id}")
        self.assertEqual(reponse.status_code, 404)

    def test_route_update_objet(self):
        reponse_ex = self.objet.post(
            "/objet/", json={"libobj": "ecran", "tailleobj": 10}
        )
        self.objet_id = reponse_ex.json().get("codobj")

        update_data = {"libobj": "television"}

        reponse_update = self.objet.patch(f"/objet/{self.objet_id}", json=update_data)
        self.assertEqual(reponse_update.status_code, 200)
        self.assertIsInstance(reponse_update.json(), Dict)

        clés = {
            "libobj",
            "tailleobj",
            "puobj",
            "poidsobj",
            "indispobj",
            "o_imp",
            "o_aff",
            "o_cartp",
            "points",
            "o_ordre_aff",
            "codobj",
        }
        self.assertTrue(clés.issubset(reponse_update.json().keys()))
        self.assertEqual(reponse_update.json().get("libobj"), "television")
        self.objet.delete(f"/objet/{reponse_update.json()['codobj']}")

    def test_update_objet_not_found(self):
        invalid_objet_id = 999999
        update_data = {"libobj": "televisionCassee"}
        reponse_update = self.objet.patch(
            f"/objet/{invalid_objet_id}", json=update_data
        )
        self.assertEqual(reponse_update.status_code, 404)


if __name__ == "__main__":
    unittest.main()
