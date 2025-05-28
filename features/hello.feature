Feature: Hello endpoint

  Scenario: Saying hello to a named user
    Given the API is running
    When I GET "/hello?name=Omar"
    Then the response should contain "Hello, Omar!"
