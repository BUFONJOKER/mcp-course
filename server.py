from fastmcp.server import create_proxy
app = create_proxy(
    {
        "mcpServers": {
            "default": {
                "command": "npx",
                "args": [
                    "-y",
                    "mcp-remote",
                    "https://expensetrackerappmcp.fastmcp.app/mcp",
                ],
            }
        }
    },
    name="MyProxyExpenseTrackerMCPServer",
)


if __name__ == "__main__":
    app.run()