from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

HORIZON_TOKEN = os.getenv("HORIZON_TOKEN")

if not HORIZON_TOKEN:
    print("Warning: HORIZON_TOKEN is not set!")

SERVERS = {
    "My First Simple FastMCP App": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "D:\\Data-Science\\mcp-course\\main.py"
      ],
      "env": {},
      "transport": "stdio"
  },
    "Expense Tracker MCP (Hosted)": {
        "url": "https://expensetrackerappmcp.fastmcp.app/mcp",
        "transport": "streamable_http",
        "headers": {
            "Authorization": f"Bearer {HORIZON_TOKEN}" #
        }
    }

}

async def main():

  client = MultiServerMCPClient(SERVERS)
  tools = await client.get_tools()

  named_tools = {tool.name: tool for tool in tools}

  model = ChatOllama(model="qwen3.5:cloud")
  model_with_tools = model.bind_tools(tools)

  prompt = "Generate a random number"
  response = await model_with_tools.ainvoke(prompt)
  print("Response:", response)

if __name__ == "__main__":
    asyncio.run(main())