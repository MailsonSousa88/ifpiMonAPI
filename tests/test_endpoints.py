from http import HTTPStatus
from unittest import TestCase

from fastapi.testclient import TestClient

from api.main import app


class TestEndpoints(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    def test_root(self) -> None:
        response = self.client.get("/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json()["ifpimons"], "/api/ifpimons")

    def test_get_all_ifpimons(self) -> None:
        response = self.client.get("/api/ifpimons")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIsInstance(response.json(), list)
        self.assertGreater(len(response.json()), 0)

    def test_get_ifpimon_by_id(self) -> None:
        response = self.client.get("/api/ifpimons/1")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json()["id"], 1)

    def test_get_unknown_ifpimon(self) -> None:
        response = self.client.get("/api/ifpimons/999")

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.assertEqual(response.json()["error"], "ifpimon_not_found")

    def test_get_ifpimon_with_invalid_id(self) -> None:
        response = self.client.get("/api/ifpimons/abc")

        self.assertEqual(
            response.status_code,
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )
