from fastmcp import FastMCP
import os
import sqlite3

mcp = FastMCP(name='Expense Tracker MCP Server')

# This ensures the DB is always created in the same folder as main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "expenses.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_table():
    with get_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                subcategory TEXT DEFAULT ''
            )
        ''')

create_table()

@mcp.tool
def list_expenses(date_from: str = '', date_to: str = ''):
    """Lists all expenses in given date range if data given otherwise all expense."""
    with get_connection() as conn:
        if date_from and date_to:
            cursor = conn.execute('''
                SELECT * FROM expenses
                WHERE date BETWEEN ? AND ?
                ORDER BY date DESC
            ''', (date_from, date_to))
        else:
            cursor = conn.execute('''
                SELECT * FROM expenses
                ORDER BY date DESC
            ''')
        expenses = cursor.fetchall()
    return expenses

@mcp.tool
def add_expense(date: str, amount: float, category: str, subcategory: str = ''):
    """Adds a new expense to the database."""
    with get_connection() as conn:
        conn.execute('''
            INSERT INTO expenses (date, amount, category, subcategory)
            VALUES (?, ?, ?, ?)
        ''', (date, amount, category, subcategory))
        conn.commit()
    return "Expense added successfully."

if __name__ == "__main__":
    mcp.run()