@echo off
set PATH=%PATH%;C:\Users\malik\AppData\Roaming\Python\Python311\Scripts
@REM call venv\Scripts\activate
pytest -s -v -m "sanity" --html reports/sanity_test_report.html .\test_cases --browser chrome
pytest -s -v -m "sanity and regression" --html reports/sanity_and_regression_report.html .\test_cases --browser chrome
pause