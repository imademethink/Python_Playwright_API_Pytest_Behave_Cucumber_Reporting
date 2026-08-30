import json
from profile_api.API00_Base import BaseAPIPrep


class APILogin(BaseAPIPrep):
    def __init__(self, context):
        self.context = context
        self.test_data = None

    def prep_header(self):
        print("    APILogin:: prep_header")
        self.context.headers = {}
        self.test_data = self.context.global_handle
        print("    Header json:\n" + json.dumps(self.context.headers, indent=4))

    def prep_body(self):
        print("    APILogin:: prep_body")
        self.context.payload = {"email":self.test_data["email"], "password":self.test_data["password"]}
        print("    Payload json:\n" + json.dumps(self.context.payload, indent=4))

    def prep_api_call(self):
        print("    APILogin:: prep_api_call")
        self.context.response = self.context.api_request.post(
            url=self.test_data["endpoint_login"], headers=self.context.headers, data=self.context.payload)
        print("    Url: " + self.context.base_url + self.test_data["endpoint_login"])
        print("    Method: POST")

    def prep_response_validate(self, valid_user=True):
        print("    APILogin:: prep_response_process")
        response = self.context.response
        if valid_user:
            print("    Response code:\n" + str(response.status))
            assert response.status == 200
            response_json = response.json()
            print("    Response json:\n" + json.dumps(response_json, indent=4))
            assert response_json["success"] == True
            assert response_json["status"] == 200
            assert response_json["message"] == "Login successful"
            assert "id" in response_json["data"]
            assert "name" in response_json["data"]
            assert "email" in response_json["data"]
            assert "token" in response_json["data"]
            self.test_data["token"] = response_json["data"]["token"]
            print("    token: " + self.test_data["token"])
        else:
            print("    Response code:\n" + str(response.status))
            assert response.status == 401
            response_json = response.json()
            print("    Response json:\n" + json.dumps(response_json, indent=4))
            assert response_json["success"] == False
            assert response_json["status"] == 401
            assert response_json["message"] == "Incorrect email address or password"
