import json
from profile_api.API00_Base import BaseAPIPrep


class APILogout(BaseAPIPrep):
    def __init__(self, context):
        self.context = context
        self.test_data = None

    def prep_header(self):
        print("    APILogout:: prep_header")
        self.test_data = self.context.global_handle
        self.context.headers = {"X-Auth-Token": self.test_data["token"]}
        print("    Header json:\n" + json.dumps(self.context.headers, indent=4))

    def prep_body(self):
        print("    APILogout:: prep_body")
        self.context.payload = {"email":self.test_data["email"], "password":self.test_data["password"]}
        print("    Payload json:\n" + json.dumps(self.context.payload, indent=4))

    def prep_api_call(self):
        print("    APILogout:: prep_api_call")
        self.context.response = self.context.api_request.delete(
            url=self.test_data["endpoint_logout"], headers=self.context.headers, data=self.context.payload)
        print("    Url: " + self.context.base_url + self.test_data["endpoint_logout"])
        print("    Method: DELETE")

    def prep_response_validate(self):
        print("    APILogout:: prep_response_process")
        response = self.context.response
        print("    Response code:\n" + str(response.status))
        assert response.status == 200
        response_json = response.json()
        print("    Response json:\n" + json.dumps(response_json, indent=4))
        assert response_json["success"] == True
        assert response_json["status"] == 200
        assert response_json["message"] == "User has been successfully logged out"
