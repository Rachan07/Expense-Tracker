
import pandas as pd
from pathlib import Path
from datetime import date

FILE_NAME = "expenses.xlsx"

COLUMNS = ["Date", "Category", "Description", "Amount"]


# Load expenses from Excel or create a new file
def load_expenses():
    if Path(FILE_NAME).exists():
        df = pd.read_excel(FILE_NAME, sheet_name="Expenses")

        # Check that the required columns exist
        if not all(column in df.columns for column in COLUMNS):
            raise ValueError(
                "Excel file must contain: Date, Category, Description, Amount"
            )

        return df[COLUMNS]

    df = pd.DataFrame(columns=COLUMNS)
    df.to_excel(FILE_NAME, sheet_name="Expenses", index=False)
    return df


# Save expenses to Excel
def save_expenses():
    expenses.to_excel(FILE_NAME, sheet_name="Expenses", index=False)


# Display menu
def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spending")
    print("4. Exit")


# Add a new expense
def add_expense():
    global expenses

    try:
        amount = float(input("Enter expense amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category (Food, Travel, etc.): ").strip()
        description = input("Enter expense description: ").strip()

        if not category or not description:
            print("Category and description cannot be empty.")
            return

        new_expense = pd.DataFrame([{
            "Date": str(date.today()),
            "Category": category,
            "Description": description,
            "Amount": amount
        }])

        expenses = pd.concat(
            [expenses, new_expense],
            ignore_index=True
        )

        save_expenses()
        print("Expense added and saved to Excel successfully!")

    except ValueError:
        print("Invalid amount. Please enter a valid number.")


# View all expenses
def view_expenses():
    if expenses.empty:
        print("\nNo expenses added yet.")
        return

    print("\n===== YOUR EXPENSES =====")
    print(expenses.to_string(index=False))


# Calculate total spending
def show_total():
    if expenses.empty:
        print("\nNo expenses to calculate.")
        return

    total = pd.to_numeric(
        expenses["Amount"], errors="coerce"
    ).sum()

    print(f"\nTotal Spending: ₹{total:.2f}")


# Load saved data when the program starts
expenses = load_expenses()


# Main program
while True:
    show_menu()

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
