# MCP Course: FastMCP Learning Projects 🚀

Hands-on FastMCP practice repository with two Python MCP servers:

- a simple starter server for basic tools
- an Expense Tracker MCP server backed by SQLite

## ✨ Project Highlights

### 🧩 FastMCP Fundamentals

Learn how to:

- create MCP servers with `FastMCP`
- register tools using `@mcp.tool`
- expose resources using `@mcp.resource`
- run servers locally for development and testing

### 💸 Real Mini-Project

The Expense Tracker server demonstrates:

- persistent storage using SQLite
- date-range filtering
- category-wise expense summaries
- JSON resource serving via MCP

## 🧱 Tech Stack

- Python `3.11+`
- `fastmcp>=3.1.0`
- SQLite (built-in with Python)
- `uv` (recommended)

## 📂 Repository Structure

```text
mcp-course/
├── main.py
├── test.py
├── pyproject.toml
├── README.md
└── expense_tracker_mcp_server/
	├── __init__.py
	├── main.py
	└── categories.json
```

## ⚙️ Setup Guide

### 1. Clone the repository 📥

```bash
git clone https://github.com/BUFONJOKER/mcp-course.git
cd mcp-course
```

### 2. Install dependencies 📦

```bash
uv sync
```

If you are not using `uv`, create a virtual environment and install `fastmcp` manually.

## ▶️ Run the Servers

### A) Simple MCP server (root) 🎲

```bash
python main.py
```

### B) Expense Tracker MCP server 💸

```bash
python expense_tracker_mcp_server/main.py
```

### C) Run with FastMCP CLI (optional) 🛠️

```bash
uv run fastmcp run main.py
uv run fastmcp run expense_tracker_mcp_server/main.py
```

### D) Run in MCP Inspector (dev mode) 🔎

```bash
uv run fastmcp dev inspector main.py
uv run fastmcp dev inspector expense_tracker_mcp_server/main.py
```

## 🛠️ Available MCP Features

### 1) Root Server Tools (`main.py`)

#### 🎲 `generate_random_number()`

- Returns a random integer from `1` to `100`.

#### ➕ `add_two_numbers(first_number, second_number)`

- Returns the sum of two numeric inputs.

### 2) Expense Tracker Tools (`expense_tracker_mcp_server/main.py`)

#### ➕ `add_expense(date, amount, category, subcategory='')`

- Adds a new expense record.

#### 📋 `list_expenses(date_from='', date_to='')`

- Lists all expenses.
- If both dates are provided, returns expenses in that range.

#### 📊 `summarize(start_date, end_date, category='')`

- Returns total spending grouped by category.
- If a category is provided, summarizes only that category.

#### 📚 Resource: `expense://categories`

- Serves category data from `categories.json` as JSON.

## 🗄️ Data Notes

- Expense data is stored in `expense_tracker_mcp_server/expenses.db` (created automatically).
- The `expenses` table is initialized on server startup.

## 🧪 Quick Examples

- `add_two_numbers(10, 5)` → `15`
- `generate_random_number()` → any integer in `1..100`
- `add_expense("2026-03-01", 250.0, "Food", "Lunch")` → success message

## 🎯 Learning Outcomes

By working through this repo, you will practice:

- MCP tool design and registration
- working with persistent local storage
- structuring multi-module Python MCP projects
- exposing both tools and resources in one server

## 🤝 Contributing

Contributions are welcome for:

- new tools
- better validations/error handling
- improved examples and docs

## 📜 License

This repository is for learning and practice.
