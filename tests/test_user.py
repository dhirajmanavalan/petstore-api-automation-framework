import  pytest

from utils.apis import APIS

@pytest.fixture(scope="module")
def apis():
    return APIS()

@pytest.fixture(scope="module")
def user_id():
    return 1

@pytest.fixture(scope="module")
def payload(user_id):
    return {
  "id": 44,
  "username": "dhiruofflll",
  "firstName": "dinesh",
  "lastName": "kumar",
  "email": "dhi@gmail.com",
  "password": "dhi@2",
  "phone": "8489403967",
  "userStatus": 1
}

@pytest.fixture(scope="module")
def users_array():
    return [
        {
            "id": 601,
            "username": "arrayUser601",
            "firstName": "Array",
            "lastName": "User1",
            "email": "array601@gmail.com",
            "password": "pass601",
            "phone": "1111111111",
            "userStatus": 1
        },
        {
            "id": 602,
            "username": "arrayUser602",
            "firstName": "Array",
            "lastName": "User2",
            "email": "array602@gmail.com",
            "password": "pass602",
            "phone": "2222222222",
            "userStatus": 1
        }
    ]

def test_create_users_with_array(apis, users_array):
    response = apis.post("user/createWithArray", users_array)
    assert response.status_code == 200
    print(response.json())

def test_create_user(apis, payload):
    response = apis.post("user", payload)
    assert response.status_code == 200
    # assert response.json()["id"] == user_id
    print(response.json())

def test_get_user(apis, payload):
    response = apis.get(f"user/{payload['username']}")
    assert response.status_code == 200
    assert response.json()["username"] == payload["username"]
    print(response.json())

def test_update_user(apis, payload):
    data = payload.copy()
    data["firstName"] = "dhiraj"

    response = apis.put(f"user/{payload['username']}",data)
    assert response.status_code == 200
    print(response.json())

# def test_login_user(apis, payload):
#     logininfo = {
#         "username": payload["username"],
#         "password": payload["password"]
#     }
#
#     response = apis.get("user/login", params=logininfo)
#     assert response.status_code == 200
#     print(response.json())


# def test_logout_user(apis):
#     response = apis.get("user/logout")
#     assert response.status_code == 200
#     print(response.json())

def test_delete_user(apis, payload):
    response = apis.delete(f"user/{payload['username']}")
    assert response.status_code == 200
    print(response.json())