# app/tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_upload_file():
    with open("test_files/test.pdf", "rb") as f:
        response = client.post("/upload", files={"file": ("test.pdf", f, "application/pdf")})
    assert response.status_code == 200
    data = response.json()
    assert "file_id" in data


def test_download_file():
    # First, upload a file to ensure it exists
    with open("test_files/test.pdf", "rb") as f:
        upload_response = client.post("/upload", files={"file": ("test.pdf", f, "application/pdf")})
    file_id = upload_response.json()["file_id"]

    # Now, attempt to download the file
    response = client.get(f"/download/{file_id}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"


def test_delete_file():
    # Upload a file to delete
    with open("test_files/test.pdf", "rb") as f:
        upload_response = client.post("/upload", files={"file": ("test.pdf", f, "application/pdf")})
    file_id = upload_response.json()["file_id"]

    # Delete the file
    response = client.post("/delete", json={"file_id": file_id})
    assert response.status_code == 200
    assert response.json()["message"] == "File deleted successfully."


def test_get_file_details():
    # Upload files
    file_ids = []
    for file_name in ["test1.pdf", "test2.pdf"]:
        with open(f"test_files/{file_name}", "rb") as f:
            upload_response = client.post("/upload", files={"file": (file_name, f, "application/pdf")})
            file_ids.append(upload_response.json()["file_id"])

    # Get details
    response = client.post("/details", json={"files": file_ids})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
