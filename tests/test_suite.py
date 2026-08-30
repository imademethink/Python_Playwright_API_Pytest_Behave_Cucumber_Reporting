from faker import Faker
import pytest
from playwright.sync_api import Playwright
data_handle = {}

@pytest.fixture(scope="session")
def api_context_independent(playwright: Playwright):
    faker = Faker()
    random_email = faker.email()
    data_handle["name"] = "Mary Smith"
    data_handle["email"] = random_email
    data_handle["password"] = "Demo1234"
    data_handle["password_new"] = "Demo9999"
    data_handle["base_url"] = "https://practice.expandtesting.com/notes/api/"
    data_handle["endpoint_register"] = "users/register"
    data_handle["endpoint_login"] = "users/login"
    data_handle["endpoint_logout"] = "users/logout"
    data_handle["endpoint_profile"] = "users/profile"
    data_handle["endpoint_forgot_password"] = "users/forgot-password"
    data_handle["endpoint_change_password"] = "users/change-password"
    data_handle["endpoint_delete_account"] = "users/delete-account"

    context = playwright.request.new_context(base_url=data_handle["base_url"])

    yield context

    context.dispose()

def test_1_post_create_user(api_context_independent):
    payload = {"name":data_handle["name"],
               "email":data_handle["email"],
               "password":data_handle["password"]}
    headers = {}
    response = api_context_independent.post(url=data_handle["endpoint_register"], headers=headers, data=payload)
    # response = api_context.post(url="users/register", data=list(payload.items()))

    assert response.status == 201
    response_json = response.json()
    print("\n===>>" + str(response_json) + "<<===\n")
    assert response_json["success"] == True
    assert response_json["status"] == 201
    assert response_json["message"] == "User account created successfully"
    assert "id" in response_json["data"]

def test_2_post_user_login(api_context_independent):
    payload = {"email":data_handle["email"], "password":data_handle["password"]}
    headers = {}
    response = api_context_independent.post(url=data_handle["endpoint_login"], headers=headers, data=payload)
    assert response.status == 200
    response_json = response.json()
    print("\n===>>" + str(response_json) + "<<===\n")
    assert response_json["success"] == True
    assert response_json["status"] == 200
    assert response_json["message"] == "Login successful"
    assert "id" in response_json["data"]
    assert "name" in response_json["data"]
    assert "email" in response_json["data"]
    assert "token" in response_json["data"]
    data_handle["token"] = response_json["data"]["token"]
    print("token: " + data_handle["token"])

def test_3_delete_user_logout(api_context_independent):
    payload = {"email":data_handle["email"], "password":data_handle["password"]}
    headers = {"X-Auth-Token": data_handle["token"]}
    response = api_context_independent.delete(url=data_handle["endpoint_logout"], headers=headers, data=payload)
    assert response.status == 200
    response_json = response.json()
    print("\n===>>" + str(response_json) + "<<===\n")
    assert response_json["success"] == True
    assert response_json["status"] == 200
    assert response_json["message"] == "User has been successfully logged out"

def test_4_get_user_profile(api_context_independent):
    payload = {"email":data_handle["email"], "password":data_handle["password"]}
    headers = {}
    # login
    response = api_context_independent.post(url=data_handle["endpoint_login"], headers=headers, data=payload)
    assert response.status == 200
    response_json = response.json()
    data_handle["token"] = response_json["data"]["token"]
    # get profile
    payload.clear()
    headers = {"X-Auth-Token": data_handle["token"]}
    response = api_context_independent.get(url=data_handle["endpoint_profile"], headers=headers, data=payload)
    response_json = response.json()
    print("\n===>>" + str(response_json) + "<<===\n")
    assert response_json["success"] == True
    assert response_json["status"] == 200
    assert response_json["message"] == "Profile successful"
    assert "id" in response_json["data"]
    assert "name" in response_json["data"]
    assert "email" in response_json["data"]

def test_5_post_forgot_password(api_context_independent):
    payload = {"email":data_handle["email"], "password":data_handle["password"]}
    headers = {}
    # login
    response = api_context_independent.post(url=data_handle["endpoint_login"], headers=headers, data=payload)
    assert response.status == 200
    response_json = response.json()
    data_handle["token"] = response_json["data"]["token"]
    # forget password
    payload.clear()
    payload = {"email":data_handle["email"]}
    headers.clear()
    headers = {"X-Auth-Token": data_handle["token"]}
    response = api_context_independent.post(url=data_handle["endpoint_forgot_password"], headers=headers, data=payload)
    response_json = response.json()
    print("\n===>>" + str(response_json) + "<<===\n")
    assert response_json["success"] == True
    assert response_json["status"] == 200
    assert "Password reset link successfully sent to" in response_json["message"]

def test_6_post_change_password(api_context_independent):
    payload = {"email":data_handle["email"], "password":data_handle["password"]}
    headers = {}
    # login
    response = api_context_independent.post(url=data_handle["endpoint_login"], headers=headers, data=payload)
    assert response.status == 200
    response_json = response.json()
    data_handle["token"] = response_json["data"]["token"]
    # change password
    payload.clear()
    headers.clear()
    payload = {"currentPassword":data_handle["password"], "newPassword":data_handle["password_new"]}
    headers = {"X-Auth-Token": data_handle["token"]}
    response = api_context_independent.post(url=data_handle["endpoint_change_password"], headers=headers, data=payload)
    response_json = response.json()
    print("\n===>>" + str(response_json) + "<<===\n")
    assert response_json["success"] == True
    assert response_json["status"] == 200
    assert response_json["message"] == "The password was successfully updated"

def test_7_delete_account(api_context_independent):
    payload = {"email":data_handle["email"], "password":data_handle["password_new"]}
    headers = {}
    # login
    response = api_context_independent.post(url=data_handle["endpoint_login"], headers=headers, data=payload)
    assert response.status == 200
    response_json = response.json()
    data_handle["token"] = response_json["data"]["token"]
    #
    headers.clear()
    headers = {"X-Auth-Token": data_handle["token"]}
    response = api_context_independent.delete(url=data_handle["endpoint_delete_account"], headers=headers)
    assert response.status == 200
    response_json = response.json()
    print("\n===>>" + str(response_json) + "<<===\n")
    assert response_json["success"] == True
    assert response_json["status"] == 200
    assert response_json["message"] == "Account successfully deleted"

#   pytest tests/ --alluredir=allure-report
