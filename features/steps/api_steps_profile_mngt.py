from behave import given, when, then

from features.environment import GeneralObjects
from profile_api.API01_Registration import APIRegistration
from profile_api.API02_Login import APILogin
from profile_api.API03_Logout import APILogout
from profile_api.API04_GetProfile import APIGetProfile
from profile_api.API05_ForgetPassword import APIForgetPassword
from profile_api.API06_ChangePassword import APIChangePassword
from profile_api.API07_DeleteAccount import APIDeleteAccount


@given('Complete formal registration')
def step_impl(context):
    print("    Step:: Complete formal registration")
    assert context.api_request is not None, "Playwright API context failed to initialize."
    general_objects = GeneralObjects()
    api_register = APIRegistration(context)
    general_objects.api_register = api_register
    api_register.prep_header()
    api_register.prep_body()
    api_register.prep_api_call()
    api_register.prep_response_validate()

@when('Process profile login')
def step_impl(context):
    print("    Step:: Process profile login")
    general_objects = GeneralObjects()
    api_login = APILogin(context)
    general_objects.api_login = api_login
    api_login.prep_header()
    api_login.prep_body()
    api_login.prep_api_call()

@then('Validate response for login')
def step_impl(context):
    print("    Step:: Validate response for login")
    general_objects = GeneralObjects()
    api_login = general_objects.api_login
    api_login.prep_response_validate()

@when('Complete formal login')
def step_impl(context):
    print("    Step:: Complete formal login")
    general_objects = GeneralObjects()
    api_login = APILogin(context)
    general_objects.api_login = api_login
    api_login.prep_header()
    api_login.prep_body()
    api_login.prep_api_call()
    api_login.prep_response_validate()

@when('Process profile logout')
def step_impl(context):
    print("    Step:: Process profile logout")
    general_objects = GeneralObjects()
    api_logout = APILogout(context)
    general_objects.api_logout = api_logout
    api_logout.prep_header()
    api_logout.prep_body()
    api_logout.prep_api_call()

@then('Validate response for logout')
def step_impl(context):
    print("    Step:: Validate response for logout")
    general_objects = GeneralObjects()
    api_logout = general_objects.api_logout
    api_logout.prep_response_validate()

@when('Complete formal logout')
@then('Complete formal logout')
def step_impl(context):
    print("    Step:: Complete formal logout")
    general_objects = GeneralObjects()
    api_logout = APILogout(context)
    general_objects.api_logout = api_logout
    api_logout.prep_header()
    api_logout.prep_body()
    api_logout.prep_api_call()
    api_logout.prep_response_validate()

@when('Process get profile')
def step_impl(context):
    print("    Step:: Process get profile")
    general_objects = GeneralObjects()
    api_get_profile = APIGetProfile(context)
    general_objects.api_get_profile = api_get_profile
    api_get_profile.prep_header()
    api_get_profile.prep_body()
    api_get_profile.prep_api_call()

@then('Validate response for get profile')
def step_impl(context):
    print("    Step:: Validate response for get profile")
    general_objects = GeneralObjects()
    api_get_profile = general_objects.api_get_profile
    api_get_profile.prep_response_validate()

@when('Process forget password')
def step_impl(context):
    print("    Step:: Process forget password")
    general_objects = GeneralObjects()
    api_forget_password = APIForgetPassword(context)
    general_objects.api_forget_password = api_forget_password
    api_forget_password.prep_header()
    api_forget_password.prep_body()
    api_forget_password.prep_api_call()

@then('Validate response for forget password')
def step_impl(context):
    print("    Step:: Validate response for forget password")
    general_objects = GeneralObjects()
    api_forget_password = general_objects.api_forget_password
    api_forget_password.prep_response_validate()

@when('Process change password')
def step_impl(context):
    print("    Step:: Process change password")
    general_objects = GeneralObjects()
    api_change_password = APIChangePassword(context)
    general_objects.api_change_password = api_change_password
    api_change_password.prep_header()
    api_change_password.prep_body()
    api_change_password.prep_api_call()

@then('Validate response for change password')
def step_impl(context):
    print("    Step:: Validate response for change password")
    general_objects = GeneralObjects()
    api_change_password = general_objects.api_change_password
    api_change_password.prep_response_validate()

@when('Process delete account')
def step_impl(context):
    print("    Step:: Process delete account")
    general_objects = GeneralObjects()
    api_delete_account = APIDeleteAccount(context)
    general_objects.api_delete_account = api_delete_account
    api_delete_account.prep_header()
    api_delete_account.prep_body()
    api_delete_account.prep_api_call()

@then('Validate response for delete account')
def step_impl(context):
    print("    Step:: Validate response for delete account")
    general_objects = GeneralObjects()
    api_delete_account = general_objects.api_delete_account
    api_delete_account.prep_response_validate()

@then('Validate response for invalid login')
def step_impl(context):
    print("    Step:: Validate response for invalid login")
    general_objects = GeneralObjects()
    api_login = APILogin(context)
    general_objects.api_login = api_login
    api_login.prep_header()
    api_login.prep_body()
    api_login.prep_api_call()
    api_login.prep_response_validate(valid_user=False)
