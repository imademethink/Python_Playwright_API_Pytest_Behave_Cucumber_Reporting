import json
from profile_api.API00_Base import BaseAPIPrep


class APIRegistration(BaseAPIPrep):
    def __init__(self, context):
        self.context = context
        self.test_data = None

    def prep_header(self):
        print("    APIRegistration:: prep_header")
        self.context.headers = {}
        self.test_data = self.context.global_handle
        print("    Header json:\n" + json.dumps(self.context.headers, indent=4))

    def prep_body(self):
        print("    APIRegistration:: prep_body")
        self.context.payload = {"name":self.test_data["name"],
                                "email":self.test_data["email"],
                                "password":self.test_data["password"]}
        print("    Payload json:\n" + json.dumps(self.context.payload, indent=4))

    def prep_api_call(self):
        print("    APIRegistration:: prep_api_call")
        self.context.response = self.context.api_request.post(
            url=self.test_data["endpoint_register"],
            headers=self.context.headers,
            data=self.context.payload
        )
        print("    Url: " + self.context.base_url + self.test_data["endpoint_register"])
        print("    Method: POST")

    def prep_response_validate(self):
        print("    APIRegistration:: prep_response_process")
        response = self.context.response
        print("    Response code:\n" + str(response.status))
        assert response.status == 201
        response_json = response.json()
        print("    Response json:\n" + json.dumps(response_json, indent=4))
        assert response_json["success"] == True
        assert response_json["status"] == 201
        assert response_json["message"] == "User account created successfully"
        assert "id" in response_json["data"]
