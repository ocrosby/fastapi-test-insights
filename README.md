# 🚀 fastapi-test-insights

[![Tests](https://github.com/ocrosby/fastapi-test-insights/actions/workflows/test.yml/badge.svg)](https://github.com/ocrosby/fastapi-test-insights/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**fastapi-test-insights** is a RESTful API built with [FastAPI](https://fastapi.tiangolo.com/) for collecting, storing, and serving test suite results, including those parsed from `junit.xml` files. It supports behavior-driven development (BDD) with `pytest-bdd` and integrates seamlessly with Allure for rich test reporting and insights.

---

## 📦 Features

* Ingests and parses `junit.xml` files from test suite runs
* Stores metadata for test suites and individual test cases
* Exposes a clean REST API to upload, retrieve, and manage test run data
* Uses `pytest-bdd` for behavioral testing
* Supports Allure reports via `allure-pytest` and `allure-python-commons`
* Developer automation via `invoke`

---

## 🧱 Tech Stack

* **FastAPI** for RESTful API development
* **Pydantic** for data modeling and validation
* **Pytest + BDD** for test automation
* **Allure** for test report generation
* **Invoke** for task automation
* **Flit** for lightweight packaging

---

## 📁 Project Structure

```
fastapi-test-insights/
├── app/                  # Application code
│   ├── main.py           # FastAPI app
│   ├── models.py         # Pydantic models
│   ├── routes/           # API endpoints
│   └── parsers/          # XML parsing utilities
├── tests/                # pytest-bdd tests and step definitions
│   ├── features/
│   ├── steps/
├── requirements.txt      # Optional for quick installs
├── pyproject.toml        # Flit + dependency management
├── tasks.py              # Invoke automation tasks
└── README.md             # You're reading it!
```

---

## 🚀 Quickstart

### 🔧 Install Dependencies

Install [Flit](https://flit.pypa.io/en/stable/) if not already:

```bash
pip install flit
```

Install the project (with symlink for local development):

```bash
flit install --symlink --deps=develop
```

---

## 🧪 Run Tests

Run the test suite with Allure output:

```bash
inv test
```

Serve Allure report in browser:

```bash
inv report
```

---

## 📂 Upload a JUnit XML

Example endpoint to parse and store test results:

```bash
curl -X POST http://localhost:8000/results/upload \
  -F "file=@junit.xml"
```

---

## ⚙️ Developer Tasks

| Task         | Description                 |
| ------------ | --------------------------- |
| `inv run`    | Run the FastAPI application |
| `inv test`   | Execute pytest suite        |
| `inv report` | Launch Allure report UI     |
| `inv lint`   | Run flake8 for code linting |
| `inv format` | Format code using black     |

---

## 🧪 BDD Testing

This project uses [pytest-bdd](https://pytest-bdd.readthedocs.io/) to test API behaviors via Gherkin-style feature files.

Example feature:

```gherkin
Feature: Test metadata API

  Scenario: Get test metadata
    Given the API is running
    When I request metadata for test ID "123"
    Then the response should contain the test name "Login test"
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome! Please:

1. Fork the repo
2. Create a feature branch
3. Follow existing style conventions (`black`, `flake8`)
4. Write or update relevant tests
5. Submit a PR with a clear description

---

## 📬 Contact

Created and maintained by **Omar Crosby**
Questions, issues, or suggestions? Feel free to open an [issue](https://github.com/ocrosby/fastapi-test-insights/issues).

---
