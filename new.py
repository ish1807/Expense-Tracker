import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# File to store expenses
CSV_FILE = 'expenses.csv'

# Function to add an expense
def add_expense(date, amount, category):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])
    messagebox.showinfo("Success", "Expense added successfully!")

# Function to view all expenses
def view_expenses():
    expenses_window = tk.Toplevel()
    expenses_window.title("View Expenses")
    
    tree = ttk.Treeview(expenses_window, columns=('Date', 'Amount', 'Category'), show='headings')
    tree.heading('Date', text='Date')
    tree.heading('Amount', text='Amount')
    tree.heading('Category', text='Category')
    tree.pack(fill=tk.BOTH, expand=True)

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            tree.insert('', tk.END, values=row)

# Function to analyze expenses
def analyze_expenses():
    total_expense = 0
    expense_count = 0
    category_totals = {}

    with open(CSV_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            amount = float(row[1])
            category = row[2]
            total_expense += amount
            expense_count += 1
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
    
    analysis_window = tk.Toplevel()
    analysis_window.title("Expense Analysis")
    
    if expense_count > 0:
        analysis_label = tk.Label(analysis_window, text=f"Total Expenses: ${total_expense:.2f}\nAverage Expense: ${total_expense/expense_count:.2f}\n")
        analysis_label.pack()
        
        for category, total in category_totals.items():
            category_label = tk.Label(analysis_window, text=f"{category}: ${total:.2f}")
            category_label.pack()
    else:
        tk.Label(analysis_window, text="No expenses recorded yet.").pack()

# Main application window
def main():
    root = tk.Tk()
    root.title("Personal Expense Tracker")

    tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10)
    date_entry = tk.Entry(root)
    date_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Amount:").grid(row=1, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(root)
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Category:").grid(row=2, column=0, padx=10, pady=10)
    category_entry = tk.Entry(root)
    category_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(root, text="Add Expense", command=lambda: add_expense(date_entry.get(), amount_entry.get(), category_entry.get())).grid(row=3, column=0, padx=10, pady=10)
    tk.Button(root, text="View Expenses", command=view_expenses).grid(row=3, column=1, padx=10, pady=10)
    tk.Button(root, text="Analyze Expenses", command=analyze_expenses).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
