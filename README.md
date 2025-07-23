# nopCommerce Selenium Automation Framework

A Python-based Selenium automation framework for testing the nopCommerce admin portal. This project uses the Page Object Model (POM) design pattern for maintainable and scalable test automation.

## Features

- **Page Object Model (POM):** Clean separation of page structure and test logic.
- **Selenium WebDriver:** Automates browser interactions.
- **Cross-browser support:** Easily switch between Chrome and undetected Chrome.
- **Pytest Integration:** Simple and powerful test execution.
- **Easy to extend:** Add new page objects and test cases as needed.

## Project Structure

```
nopcommerce-selenium-framework/
│
├── base_pages/
│   └── Login_Admin_Page.py      # Page object for admin login
├── test_cases/
│   └── test_admin_login.py      # Test cases for admin login
├── requirements.txt             # Project dependencies
└── README.md
```

## Getting Started

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/nopcommerce-selenium-framework.git
    cd nopcommerce-selenium-framework
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run tests:**
    ```sh
    pytest -v -s
    ```

    ```sh
    pytest -v -s .\test_cases\which_file_you_want_to_execute.py --browser firefox
    ```
    

    <!-- run multiple tests -->
    ```sh
    pytest -v -s .\test_cases\which_file_you_want_to_execute.py -n 2
    ```

    <!-- to generate HTML reports -->
    ```sh
    pytest -s -v --html reports/report.html
    ```

    <!-- data driven testing -->
    ```sh
    pytest -s -v --html reports/report.html .\test_cases\test_admin_login_data_driven.py
    ```



## Requirements

See [requirements.txt](requirements.txt) for the full list.