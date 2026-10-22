# Python Expense Tracker

## About the Project
The Python Expense Tracker is a beginner-level project designed to manage daily expenses through a simple, menu-driven command-line interface. It allows users to add expenses, view saved records, and calculate total spending.

The application uses **Pandas** to organize expense data and **Excel (.xlsx)** for persistent storage, allowing records to remain available after the program is closed.

## Features
- Add expenses with category, description, amount, and date.
- View all recorded expenses.
- Calculate total spending.
- Validate expense amounts and required fields.
- Store and retrieve expense records using Excel.

## Technologies Used
- Python
- Pandas
- OpenPyXL
- Microsoft Excel

## How to Run
1. Install Python.
2. Install the required libraries:
   ```bash
   pip install pandas openpyxl
   ```
3. Place `expense_tracker.py` and `expenses.xlsx` in the same folder.
4. Run the application:
   ```bash
   python expense_tracker.py
   ```

## Learning Outcomes
This project helped me practice Python functions, exception handling, data validation, tabular data management, and Excel file operations.

## Future Improvements
- Add category-wise spending reports.
- Add monthly expense summaries.
- Export spending reports to Excel.
- Implement automated tests and improve error handling.
