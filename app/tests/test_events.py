import os
from dotenv import load_dotenv
from unittest.mock import Mock, patch

from app.main import app
from app.core.db.session import Base
from app.core.db.mock_session import engine, client

load_dotenv(".env")

# It drops everything from the db and then recreate each time tests runs
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


X_TOKEN = os.environ["X_TOKEN"]
HEADERS = {"X-Token": X_TOKEN}
ENDPOINT = "/api/events"
LAST_RECORD_ID = 1
PAYLOAD = {
    "name": "Cool Karoke Event",
    "description": "Come get your inner rock on while singing some of the best tunes around at music karoke.",
}


# write test for healthcheck
def test_healthcheck(client):
    """
    Test if the healthcheck endpoint is working
    """
    response = client.get("/api/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "Ok"}


def test_invalid_x_token(client):
    """
    Test if it the endpoint is invalid without the token
    """
    response = client.get(ENDPOINT, params=PAYLOAD)
    assert response.status_code == 422


def test_add_event(client):
    """
    Tests if the events are being added to the database
    """

    response = client.post(ENDPOINT, json=PAYLOAD, headers=HEADERS)
    data = response.json()

    # validates if the request was successfull
    assert response.status_code == 201

    print(data)

    # validates the saved record
    assert ("name" in data) and ("description" in data)


def test_get_event(client):
    """
    Tests if the events get request is successfull
    """

    response = client.get(ENDPOINT, headers=HEADERS)

    LAST_RECORD_ID = response.json()[-1]["id"]

    # validates if the request was successfull
    assert response.status_code == 200


def test_add_invalid_event(client):
    """
    Tests if it validates the inavlid payload
    """

    invalid_payload = PAYLOAD.copy()
    invalid_payload.pop("name", None)

    response = client.post(ENDPOINT, json=invalid_payload, headers=HEADERS)

    # validates if the request was invalid because of inappropriate data
    assert response.status_code == 422


def test_update_event(client):
    """
    Tests if the event is being updated
    """

    updated_payload = PAYLOAD.copy()
    updated_payload["name"] = "New Karoke Event"
    response = client.put(
        f"{ENDPOINT}/{LAST_RECORD_ID}", json=updated_payload, headers=HEADERS
    )

    # validates if the request was successfull
    assert response.status_code == 201


def test_invalid_update_event(client):
    """
    Tests if it doesn't update with invalid id
    """

    updated_payload = PAYLOAD.copy()
    updated_payload["name"] = "New Karoke Event"
    response = client.put(f"{ENDPOINT}/12345", json=updated_payload, headers=HEADERS)

    # validates if the it threw an error on invalid id
    assert response.status_code == 404


def test_delete_event(client):
    """
    Tests if the event is being deleted
    """

    response = client.delete(f"{ENDPOINT}/{LAST_RECORD_ID}", headers=HEADERS)

    # validates if the request was successfull
    assert response.status_code == 204


def test_invalid_delete_event(client):
    """
    Tests if it doesn't delete with invalid id
    """

    response = client.delete(f"{ENDPOINT}/12345", headers=HEADERS)

    # validates if the it threw an error on invalid id
    assert response.status_code == 404
