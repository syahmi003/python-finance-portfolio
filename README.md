# Python Finance & Studio Automation Portfolio

A collection of practical Python command-line tools built to solve everyday personal finance tracking, investment forecasting, and media studio file management workflows.

---

## Projects Included

### 1. Compound Interest & Investment Simulator (`investment_simulator.py`)
An interactive financial projection tool that calculates year-by-year investment growth using monthly compounding (suitable for long-term savings instruments such as ASB, Tabung Haji, or unit trusts).
* **Key Features:** Calculates cumulative principal, annual dividend returns, and ending portfolio balance with formatted tabular terminal output and input validation.
* **How to Run:** `python investment_simulator.py`

### 2. Personal Cashflow & 50/30/20 Budget Analyzer (`budget_analyzer.py`)
A CSV-driven expense auditing script that categorizes monthly spending into **Needs (50%)**, **Wants (30%)**, and **Savings (20%)** against a user's monthly net income.
* **Key Features:** Parses structured CSV transaction records (`sample_expenses.csv` included for instant testing), computes actual vs. target allocation percentages, and flags overspending or low savings rates.
* **How to Run:** `python budget_analyzer.py`

### 3. Automated Studio Media & Document Organizer (`studio_file_organizer.py`)
An OS-level automation utility designed for content creators and media production teams to declutter messy directories in seconds.
* **Key Features:** Scans a target folder and automatically sorts loose files into categorized subdirectories (`Videos`, `Audio_Podcasts`, `Images_Thumbnails`, `Documents_Reports`, and `Others`) with built-in overwrite protection and confirmation prompts.
* **How to Run:** `python studio_file_organizer.py`

---

## Tech Stack & Concepts Applied
* **Language:** Python 3 (Standard Library: `csv`, `os`, `shutil`)
* **Core Concepts:** Modular function design, file I/O & CSV parsing, data structures, formatted CLI reporting, and defensive error handling (`try/except`).

---

## Author
**Muhammad Syahmi Firdaus**  
Bachelor of Information Technology (Information Assurance & Security) — IIUM
