# 🚀 Python Playwright API BDD Behave Allure/ HTML-Reporting Automation Framework

### Production-Ready Python Playwright API BDD/ Behave Automation Framework

<img width="1672" height="941" alt="Ready To Use Automation Framework - Python, Playwright, API,  Behave Cucumber, Allure Reporting" src="https://github.com/user-attachments/assets/eea11c42-2258-49da-a73e-22ba6d3d0eba" />

# YouTube Video Link

# https://youtu.be/3RMwM2HoyNk

Build reliable, maintainable, and scalable API automation using **Python, REST API, Playwright, Behave, Gherkin, and Allure/ HTML Reporting**.

⭐ If this project helps you, please consider giving it a Star!

---

# 📖 About

This repository provides a production-ready **Python Playwright API BDD/ Behave Automation Framework** built using:

* 🐍 Python
* 🌐 Playwright
* 🥒 Behave/ Cucumber
* 📝 Gherkin
* 📊 HTML Reporting
* 🧩 API Object Model
* 🪝 Behave Hooks
* 🚀 CI/CD Friendly

The framework focuses on **simplicity, readability, maintainability, and reusability** without introducing unnecessary design patterns.

It is suitable for:

* Automation Engineers
* SDET Engineers
* Software Engineers
* Beginners learning BDD automation
* Enterprise API automation projects

---

# ✨ Features

* 🐍 Python 3.x
* 🌐 Playwright
* 🥒 BDD using Behave
* 📝 Gherkin Feature Files
* 🧩 Simple API Object Model
* 📊 HTML Test Reports
* 🔄 Reusable Utilities
* 🎯 Tag-Based Test Execution
* 🧪 Positive & Negative Test Scenarios
* 🚀 CI/CD Friendly
* 🧹 Easy Maintenance
* 📁 Clean Project Structure

---

# 🏗 Framework Design

The framework intentionally follows a simple and practical architecture.

It uses:

* ✅ Real and live Project of User Profile Management via API
* ✅ API Object Model
* ✅ Behave BDD
* ✅ Gherkin language
* ✅ Reusable Utility Classes
* ✅ Separate Pytest implementation
* ✅ Hooks for Setup and Teardown
* ✅ Allure Reporting

The goal is to keep the framework:

> **Simple to understand → Easy to maintain → Easy to extend → Ready for CI/CD**

---

# 🥒 BDD with Behave

Behave enables the framework to follow **Behavior Driven Development (BDD)** using Gherkin syntax.

Example:

The Gherkin scenario is connected to Python step definitions.

```text
Feature File
     │
     ▼
Step Definitions
     │
     ▼
API Objects
     │
     ▼
Playwright Module
     │
     ▼
API End Points
```

---

# 🧩 API Object Model

The framework uses a simple **API Object Model** approach.

Each applicable API endpoint contains its:

* Individual Abstract method implementation for **Header** setup
* Individual Abstract method implementation for **Payload** setup
* Individual Abstract method implementation for **Endpoint calling** setup
* Individual Abstract method implementation for **Response Code Validation** setup
* Individual Abstract method implementation for **Response Body Validation** setup

---

# 📊 HTML Reporting

The framework supports HTML-based execution reporting.

Reports can provide:

* Test execution summary
* Passed scenarios
* Failed scenarios
* Skipped scenarios
* Scenario details
* Step execution status
* Execution duration
* Failure information
---

# 🏷 Tag-Based Test Execution

Behave tags can be used to organize and selectively execute scenarios.

Example:

```gherkin
@smoke
Scenario: Successful login
```

```gherkin
@regression
Scenario: Invalid login
```

Execute multiple tags:

```bash
behave --tags="smoke or regression"
```

---

# 📊 Data-Driven Testing

The framework is designed to easily expand for Data Driven Testing (stay  tuned).

# 📂 Project Structure

```text
Python_Playwright_API_Pytest_Behave_Cucumber_Reporting/
│
├── features/
│   │
│   ├── environment.py
│   │
│   ├── steps/
│   │   ├── login_steps.py
│   │   └── user_steps.py
│   │
│   ├── pages/
│   │   ├── login_page.py
│   │   └── home_page.py
│   │
│   ├── utils/
│   │   ├── driver_factory.py
│   │   ├── config_reader.py
│   │   ├── logger.py
│   │   └── screenshot.py
│   │
│   └── login.feature
│
├── config/
│   └── config.ini
│
├── reports/
│   ├── report.html
│   ├── screenshots/
│   └── logs/
│
├── requirements.txt
├── behave.ini
├── pytest.ini
├── .gitignore
└── README.md
```

---

# 🔄 Framework Execution Flow

```text
                 ┌──────────────────────┐
                 │   Gherkin Feature    │
                 │        File          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Behave Runner      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Step Definitions    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    API Objects      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Playwright module    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   API Endpoint       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Reports / Logs       │
                 └──────────────────────┘
```

# 💻 Prerequisites

Install the following before running the framework:

* Python 3.x
* pip
* Git
* IDE such as:

  * PyCharm
  * VS Code


# 🚀 Getting Started

Download code:

```bash
git clone https://github.com/imademethink/Python_Playwright_API_Pytest_Behave_Cucumber_Reporting.git
```

Navigate to the project:

```bash
cd Python_Playwright_API_Pytest_Behave_Cucumber_Reporting
```
Create environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run specific tests with a specific tag:

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results -f plain  --no-skipped  --no-capture --tags=@case1 
```

Run all tests:

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-report  -f plain  --no-skipped  --no-capture
```


Allure Binary intallation: Download Allure Binary from below link, Save it to a folder and add it's path in environment variable

```bash
https://github.com/allure-framework/allure2/releases
```

Generate Allure Reports:

```bash
allure serve allure-results --clean -o allure-report
```


# 🧹 Clean Framework Principles

The framework follows a few simple principles:

### Feature Files

Contain business-readable scenarios.

### Step Definitions

Contain BDD step implementations.

### Page Objects

Contain Playwright interactions.

### Utilities

Contain reusable technical functionality.

### Hooks

Contain test lifecycle operations.

### Configuration

Contains environment-specific settings. (Stay Tuned)

This separation prevents feature files from becoming tightly coupled with Playwright implementation.
---

# 📚 Learning Outcomes

This repository demonstrates:

* Python API automation
* Playwright
* BDD automation
* Behave
* Gherkin
* API Object Model
* Test lifecycle management
* Behave hooks
* HTML reporting
* Logging
* Configuration management (Stay Tuned)
* Tag-based execution
* Data-driven testing (Stay Tuned)
* Maintainable automation framework design

---

# 🎓 Suitable For

This framework can be used by:

* Beginners learning Playwright with Python
* QA Automation Engineers
* SDETs
* Software Engineers
* Test Automation Leads
* QA Managers
* Teams building BDD automation frameworks
* Teams migrating from Playwright Java to Playwright Python

---

# 🤝 Contributing

Contributions are welcome!

Feel free to:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐞 Report issues
* 💡 Suggest improvements
* 🚀 Submit Pull Requests

---

# 🗺️ Future Roadmap

Potential future enhancements:

* Database Validation
* Docker Support
* Parallel Execution
* Retry Mechanism
* GitHub Actions Pipeline
* Jenkins Pipeline
* Azure DevOps Pipeline
* Test Data Management
* Excel-Based Test Data
* JSON-Based Test Data
* Environment Management
* Advanced Failure Diagnostics

---

# 🌟 Why This Framework?

The framework is designed around a simple philosophy:

```text
Readable BDD
     +
Clean Python
     +
Reusable Page Objects
     +
Reliable Playwright
     +
Useful Reporting
     +
Simple Configuration
     =
Maintainable Automation
```

No unnecessary framework complexity.

No excessive design patterns.

Just a clean and practical automation architecture that teams can understand, maintain, and extend.

---

# 📌 Useful Commands

| Purpose              | Command                                 |
| -------------------- | --------------------------------------- |
| Install dependencies | `pip install -r requirements.txt`       |
| Run all tests        | `behave`                                |
| Run smoke tests      | `behave --tags=smoke`                   |
| Run regression       | `behave --tags=regression`              |
| Run feature          | `behave features/login.feature`         |
| Run scenario         | `behave --name "Scenario Name"`         |
| Generate HTML report | `behave -f html -o reports/report.html` |

---

# ❤️ Community

If you find this framework useful:

⭐ **Star the repository**

🍴 **Fork the repository**

🐞 **Report issues**

💡 **Suggest improvements**

🚀 **Contribute**

---

### Made with ❤️ for the Automation Testing Community

**Python • Playwright • Behave • Gherkin • BDD • HTML Reporting**
