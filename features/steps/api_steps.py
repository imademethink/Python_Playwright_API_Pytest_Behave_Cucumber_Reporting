from behave import given, when, then

@given('Prepare header and payload for registration')
def step_impl(context):
    print("Step:: Prepare header and payload for registration")
    assert context.api_request is not None, "Playwright API context failed to initialize."
    test_data = context.global_handle
    context.headers = {}
    context.payload = {"name":test_data["name"], "email":test_data["email"], "password":test_data["password"]}

@when('Call api registration')
def step_impl(context):
    print("Step:: Call api registration")
    test_data = context.global_handle
    context.response = context.api_request.post(
        url=test_data["endpoint_register"],
        headers=context.headers,
        data=context.payload)

@then('Validate response for registration')
def step_impl(context):
    print("Step:: Validate response for registration")
    response = context.response
    assert response.status == 201
    response_json = response.json()
    print(str(response_json))
    assert response_json["success"] == True
    assert response_json["status"] == 201
    assert response_json["message"] == "User account created successfully"
    assert "id" in response_json["data"]
