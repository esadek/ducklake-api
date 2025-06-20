from fastapi import status
from fastapi.testclient import TestClient

from ducklake_api.main import app


class TestQueryDucklake:
    def test_valid_query(self) -> None:
        with TestClient(app) as client:
            response = client.post(
                "/query",
                params={"sql": "SELECT 1 AS value"},
            )
            assert response.status_code == status.HTTP_200_OK
            data = response.json()
            assert data["sql"] == "SELECT 1 AS value"
            assert data["rows"] == [{"value": 1}]
            assert "timestamp" in data

    def test_invalid_query(self) -> None:
        with TestClient(app) as client:
            response = client.post(
                "/query",
                params={"sql": "foo"},
            )
            assert response.status_code == status.HTTP_400_BAD_REQUEST
            data = response.json()
            assert "detail" in data


def test_scalar_html() -> None:
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == status.HTTP_200_OK
        assert "@scalar/api-reference" in response.text
