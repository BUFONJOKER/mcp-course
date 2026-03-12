from fastmcp.server import create_proxy

# create_proxy() accepts URLs, file paths, and transports directly
app = create_proxy("https://expensetrackerappmcp.fastmcp.app/mcp", name="MyProxyExpenseTrackerMCPServer")

if __name__ == "__main__":
    app.run()