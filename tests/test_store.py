import pytest
from utils.apis import APIS
import csv
import os

@pytest.fixture(scope="module")
def apis():
    return APIS()

@pytest.fixture(scope="module")
def order_id():
    return 2

@pytest.fixture(scope="module")
def order_payload(order_id):
    return {
  "id": order_id,
  "petId": 10,
  "quantity": 4,
  "shipDate": "2026-03-03T06:19:16.847Z",
  "status": "placed",
  "complete": True
}

def test_get_inventory(apis):
    response = apis.get("store/inventory")

    assert response.status_code == 200
    print(response.json())

def test_place_order(apis, order_id, order_payload):

    pet_id = order_payload["petId"]
    pet_check_exists = apis.get(f"pet/{pet_id}")
    assert pet_check_exists.status_code == 200, "pet id not found"

    response = apis.post("store/order",order_payload)

    assert response.status_code == 200
    assert response.json()['id'] == order_id
    print(response.json())

    file_path = "data/store_orders.csv"
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["OrderID", "PetID", "Quantity", "Status"])

        writer.writerow([
            order_id,
            order_payload["petId"],
            order_payload["quantity"],
            order_payload["status"]
        ])

def test_get_order(apis, order_id):
    response = apis.get(f"store/order/{order_id}")

    assert response.status_code == 200
    assert response.json()["id"] == order_id
    print(response.json())

def test_delete_order(apis, order_id):
    response = apis.delete(f"store/order/{order_id}")

    assert response.status_code == 200

def test_verify_deleted_order(apis, order_id):
    response = apis.get(f"store/order/{order_id}")

    assert response.status_code == 404