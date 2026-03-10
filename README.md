# MCP Course Project 🚀

A simple FastMCP practice project from the CampusX MCP course.
This project exposes basic tools through an MCP server.

## 📌 Project Overview

This repository demonstrates how to:

- create an MCP server with `FastMCP`
- register tools using decorators
- run the server locally for testing and development

## 🧱 Tech Stack

- Python `3.11+`
- `fastmcp>=3.1.0`
- `uv` (recommended for environment and dependency management)

## 📂 Project Structure

```text
mcp-course/
├── main.py
├── main.ipynb
├── pyproject.toml
└── README.md
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/BUFONJOKER/mcp-course.git
cd mcp-course
```

### 2. Create environment and install dependencies

```bash
uv sync
```

If you are not using `uv`, create a virtual environment and install `fastmcp` manually.

## ▶️ Run the MCP Server

### Option A: Run directly with Python

```bash
python main.py
```

### Option B: Run with FastMCP run command

```bash
uv run fastmcp run main.py
```

### Option C: Run with MCP Inspector (dev mode)

```bash
uv run fastmcp dev inspector main.py
```

## 🛠️ Available MCP Tools

### 1) `generate_random_number()` 🎲

- Description: Generates a random integer between `1` and `100`.
- Input: None
- Output: Integer

### 2) `add_two_numbers(first_number, second_number)` ➕

- Description: Adds two numbers.
- Input: Two numeric values
- Output: Sum of the two numbers

## 🧪 Example Expectations

- `generate_random_number()` returns values in range `1..100`
- `add_two_numbers(10, 5)` returns `15`

## 🎯 Learning Goals

- understand MCP server basics
- build and expose simple tools
- practice local testing workflows

## 🤝 Contributing

Contributions are welcome for learning improvements, additional tools, and better examples.

## 📜 License

This project is for learning and practice purposes.
