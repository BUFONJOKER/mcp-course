# Expense Tracker MCP Server 💸

A lightweight MCP server for tracking expenses with SQLite, category metadata, and summary tools.

## Overview 📌

This module provides an [MCP](https://modelcontextprotocol.io) server built with FastMCP.
It supports:

- Adding expenses
- Listing expenses (optionally by date range)
- Summarizing expenses by category
- Exposing categories from a JSON resource

## Folder Structure 📂

```text
expense_tracker_mcp_server/
├── __init__.py
├── main.py
├── categories.json
├── expenses.db   # auto-created on first run
└── README.md
```

## Features ✨

### 1) Add Expense ➕

Tool: `add_expense(date, amount, category, subcategory='')`

Adds a new expense row into SQLite table `expenses`.

### 2) List Expenses 📋

Tool: `list_expenses(date_from='', date_to='')`

- If both `date_from` and `date_to` are provided, filters records using `BETWEEN`.
- Otherwise returns all expenses, sorted by date descending.

### 3) Summarize Expenses 📊

Tool: `summarize(start_date, end_date, category='')`

- Returns category-wise totals for the given date range.
- If `category` is provided, returns total for that category only.

### 4) Categories Resource 🗂️

Resource: `expense://categories`

Serves category/subcategory definitions from `categories.json` with JSON mime type.

## Database Details 🛢️

The server uses SQLite file `expenses.db` in the same folder as `main.py`.

### Table: `expenses`

| Column | Type | Notes |
|---|---|---|
| `id` | INTEGER | Primary key, auto increment |
| `date` | TEXT | Required (recommended `YYYY-MM-DD`) |
| `amount` | REAL | Required |
| `category` | TEXT | Required |
| `subcategory` | TEXT | Optional, default empty string |

## Setup ⚙️

### Prerequisites

- Python 3.10+
- `fastmcp` installed in your environment

### Install Dependencies

```bash
pip install fastmcp
```

## Run The Server ▶️

From inside this folder:

```bash
python main.py
```

On startup, the server automatically creates the `expenses` table (if missing).

## Tool Input Tips ✅

### Date Format

Use consistent date strings such as `YYYY-MM-DD` so range filters work correctly.

### Category Values

Pick `category` / `subcategory` values from `categories.json` for clean reporting.

## Example Workflow 🧪

1. Add a few expenses using `add_expense`.
2. Retrieve all records using `list_expenses`.
3. Filter by date range using `list_expenses(date_from, date_to)`.
4. Generate totals using `summarize(start_date, end_date)`.
5. Fetch valid categories from `expense://categories`.

## Notes 📝

- `expenses.db` is local to this folder.
- `__init__.py` is intentionally empty.
- Categories are maintained in `categories.json` and can be extended as needed.
