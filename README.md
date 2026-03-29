# Selenium POM Test Automation Project

UI test automation framework built with Selenium and Pytest using the Page Object Model. Includes a basic CI setup with GitHub Actions.

---

## Tech stack

* Python 3.11
* Selenium WebDriver
* Pytest
* WebDriver Manager
* GitHub Actions

---

## Overview

This project demonstrates a simple but structured approach to UI test automation. It uses the Page Object Model to keep test logic separate from page interactions and relies on explicit waits to avoid flaky tests.

The test suite covers common user flows such as registration, login, product search and cart validation.

---

## Project structure

```text
pages/        Page Object classes  
tests/        Test cases  
utils/        Test data  
conftest.py   Fixtures and setup  
.github/      CI pipeline  
```

---

## Setup

Clone the repository:

```bash
git clone https://github.com/mogyorosimartin/selenium-pom-project.git
cd selenium-pom-project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running tests

Run the full test suite:

```bash
pytest -v
```

Run only smoke tests:

```bash
pytest -m smoke
```

---

## Environment variables

Create a `.env` file in the project root:

```text
TEST_EMAIL=your_email
TEST_PASSWORD=your_password
BASE_URL=https://automationexercise.com
```

---

## CI

Tests are executed on push using GitHub Actions in a headless browser environment.

---

## Notes

* Explicit waits are used to improve stability
* Test data for registration is generated dynamically
* The structure is intended to be easy to extend

---
