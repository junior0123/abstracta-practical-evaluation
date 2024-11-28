
# Abastracta Practical Evaluation 🔍

## Introduction

This repository showcases a framework for web automation utilizing **Playwright** and **Cucumber**. It features integrated loggers and reports to enhance test visibility and management. Explore the project to understand how automated tests are structured and executed effectively.

## Prerequisites

Before you begin, ensure you have **Python** and **pip** installed on your system. You can verify your installations by running the following commands in your terminal:

```bash
python --version
pip --version
```

If Python is not installed, you can download it from [python.org](https://www.python.org/downloads/). Pip is generally installed automatically with Python.

## Setting Up the Virtual Environment 🛠️

1. **Clone the repository:**

   ```bash
   git clone git@github.com:junior0123/abstracta-practical-evaluation.git
   ```
   ```bash
   cd abstracta-practical-evaluation
   ```

2. **Create a virtual environment:**

   In your terminal, navigate to the project directory and run:

   ```bash
   python -m venv env
   ```

   This command creates a new virtual environment named `env` in your current directory.

3. **Activate the virtual environment:**

   - On **Windows**:

     ```bash
     env\Scripts\activate
     ```

   - On **macOS** and **Linux**:

     ```bash
     source env/bin/activate
     ```

   Activating the virtual environment ensures that the installed libraries and Python commands run within this isolated environment.

## Installing Dependencies 📦

1. **Install project dependencies:**

   Once the virtual environment is activated, install the required libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   playwright install
   ```

## Running the Project 🚀

To run the project follow these steps:

## Configuring Execution:

To configure the execution, create a `.env` file in the root project with the following parameters, for example:

```env
BASE_URL=https://demoblaze.com
USER=123
PASSWORD=123
NAME=PEPE
COUNTRY=BOLIVIA
CITY=CBBA
CREDIT_CARD_NUMBER="123456456-4123131"
MONTH=04
YEAR=2024
```

You can also add additional tests in the `/features/scenarios` directory to extend the test suite.
1. **Run the main script:**

   ```bash
   pytest
   ```

   This command will start the execution of all test in headed mode. 

2. **Running Tests by Marker:**

   You can also execute tests based on specific markers. Here are some examples:

   - **Purchase Tests:**  
     ```bash
     pytest -m purchase
     ```

   - **Cart Tests:**  
     ```bash
     pytest -m cart
     ```

   - **Scrape Tests:**  
     ```bash
     pytest -m scrape
     ```



# Test Suite for DemoBlaze

## Test Case Specific Markers:

- **test_01:** This test case ensures that a product can be successfully added to the cart, purchased, and confirmation details are shown.
    ```bash
    pytest -m test_01
    ```

- **test_02:** This test case verifies that products in the cart remain even after logging out and logging back in.
    ```bash
    pytest -m test_02
    ```

- **test_03:** This test case checks that products can be removed from the cart correctly.
    ```bash
    pytest -m test_03
    ```

- **test_04:** This test case tests the functionality of scraping product data (such as name and price) from multiple pages on the homepage.
    ```bash
    pytest -m test_04
    ```

## Running Tests with Different Browsers:

To run tests with different browsers, use the `--browser` parameter in the CLI:

```bash
pytest --browser webkit
```

```bash
pytest --browser firefox
```

```bash
pytest --browser chromium
```

To run in **headed** mode (with a graphical interface), use the `--headed` option:

```bash
pytest --headed
```

The program executes in **headed mode** by default (without a graphical interface) unless you specify otherwise.

You can also combine as for example:
```bash
pytest --headed --browser webkit
```
## Viewing Results:
The result of the scraping will generate a `scraped_data.txt` file in the root of the project.
Test results are generated in the `/reports` folder. Open `report.html` to access detailed test outcomes. If any issues arise, check the logs in the `/log` directory. 

## About the Author 👨‍💻

This project was created by **Alvaro Sivila**, a dedicated QA Automation Engineer with expertise in various automation tools and frameworks. If you're interested in my work, feel free to check out my portfolio or connect with me on LinkedIn:

- **Portfolio:** [Portfolio](https://junior0123.github.io/QAPortfolio/)
- **LinkedIn:** [Alvaro Sivila](https://www.linkedin.com/in/alvaro-sivila-ram%C3%ADrez-0a8537113/)


