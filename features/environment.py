from faker import Faker
from playwright.sync_api import sync_playwright


class GeneralObjects:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GeneralObjects, cls).__new__(cls)
        return cls._instance

def before_scenario(context, scenario):
    print("\n" * 5)
    context.playwright = sync_playwright().start()
    context.base_url = "https://practice.expandtesting.com/notes/api/"
    context.api_request = context.playwright.request.new_context(base_url=context.base_url, extra_http_headers={"Content-type": "application/json; charset=UTF-8", "Accept": "application/json"})

    test_data = {}
    faker = Faker()
    random_email = faker.email()
    test_data["name"] = "Jon Doe"
    test_data["email"] = random_email
    test_data["password"] = "Demo1234"
    test_data["password_new"] = "Demo9999"
    test_data["base_url"] = "https://practice.expandtesting.com/notes/api/"
    test_data["endpoint_register"] = "users/register"
    test_data["endpoint_login"] = "users/login"
    test_data["endpoint_logout"] = "users/logout"
    test_data["endpoint_profile"] = "users/profile"
    test_data["endpoint_forgot_password"] = "users/forgot-password"
    test_data["endpoint_change_password"] = "users/change-password"
    test_data["endpoint_delete_account"] = "users/delete-account"
    if not hasattr(context, 'extracted_data'):
        context.global_handle = test_data

def after_scenario(context, scenario):
    context.api_request.dispose()
    context.playwright.stop()
