Feature: User profile management simple

  @simple
  Scenario: Registration validation
    Given Prepare header and payload for registration
    When Call api registration
    Then Validate response for registration

# behave -f allure_behave.formatter:AllureFormatter -o allure-results -f plain  --no-skipped  --no-capture --tags=@simple

# allure serve allure-results --clean -o allure-report

