\# ShopQA — E-Commerce Automation Suite



Test automation framework built with Python, Selenium, and Behave (Cucumber) using the Page Object Model.



\---



\## Tech Stack



\- Python 3.14

\- Selenium WebDriver 4.25

\- Behave (Cucumber for Python)

\- Page Object Model

\- Excel + HTML reports



\---



\## Project Structure

qa-assignment-v2/

├── app/ # ShopQA web app (test target)

├── features/ # BDD .feature files

├── features/steps/ # Step definitions

├── pages/ # Page Object Model

├── utils/ # Driver factory, waits, config

├── config/ # config.ini

├── tools/ # Report generator

├── manual\_tests/ # Manual test cases

├── reports/ # Generated output

├── run\_tests.py # One-command runner

├── behave.ini

├── requirements.txt

├── bug\_report.md

└── README.md



\---



\## Setup



```bash

**git clone <YOUR-REPO-URL>**

**cd qa-assignment-v2**

**python -m venv venv**

**venv\\Scripts\\activate**

**pip install -r requirements.txt**



Run Tests

Terminal 1 — start the app:

**python -m uvicorn app.main:app --reload --port 8000**





Terminal 2 — run the tests:

**python run\_tests.py**



Reports

After the run:

**test\_report.xlsx** — all 13 test cases in a sheet

bugs.md — auto-logged defects

