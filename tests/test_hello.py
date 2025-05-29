import allure
import pytest
from pytest_bdd import scenario, given, when, then

from fastapi.testclient import TestClient


@scenario("hello.feature", "Saying hello to a named user")
def test_hello():
    pass


@given("the API is running")
def api_is_running():
    with allure.step("Start API client"):
        pass  # Placeholder


@when('I GET "/hello?name=Omar"')
def get_hello(client: TestClient):
    with allure.step("Send GET request"):
        response = client.get("/hello?name=Omar")
        client.last_response = response


@then('the response should contain "Hello, Omar!"')
def check_response(client: TestClient):
    with allure.step("Validate response"):
        response = client.last_response
        assert response.status_code == 200
        assert "Hello, Omar!" in response.json()["message"]
