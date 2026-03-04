import pytest
from utils.apis import APIS
import random
import csv
import os

@pytest.fixture(scope = "module")
def apis():
    return APIS()

@pytest.fixture(scope="module")
def pet_id():
    # return random.randint(4, 200)
    return 10

@pytest.fixture(scope="module")
def pet_payload(pet_id):
    return {
        "id": pet_id,
        "category": {"id": random.randint(15,200), "name": "Dog"},
        "name": "Brunoo",
        "photoUrls": ["Dog1"],
        "tags": [{"id": random.randint(15,200), "name": "friendly"}],
        "status": "available"
    }

def test_create_pet(apis, pet_payload, pet_id):
    response = apis.post("pet", pet_payload)

    assert response.status_code == 200
    assert response.json()["id"] == pet_id
    print(response.json())

    file_path = "data/pets_db.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["PetID", "Name", "Status"])

        writer.writerow([
            pet_id,
            pet_payload["name"],
            pet_payload["status"]
        ])

def test_update_pet(apis, pet_payload, pet_id):
    pet_payload["status"] = "sold"
    response = apis.put("pet", pet_payload)

    assert response.status_code == 200
    assert response.json()["status"] == "sold"
    print(response.json())


def test_get_pet(apis, pet_id):
    response = apis.get(f"pet/{pet_id}")

    assert response.status_code == 200
    assert response.json()["id"] == pet_id
    print(response.json())


def test_delete_pet(apis, pet_id):
    response = apis.delete(f"pet/{pet_id}")

    assert response.status_code == 200
    print(response.json())


def test_verify_deleted_pet(apis, pet_id):
    response = apis.get(f"pet/{pet_id}")

    assert response.status_code == 404
    print(response.json())
