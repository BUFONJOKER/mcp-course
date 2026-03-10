import random
from fastmcp import FastMCP

mcp = FastMCP(name='My First Simple FastMCP App')

@mcp.tool
def generate_random_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)

@mcp.tool
def add_two_numbers(first_number: float, second_number: float):
    """Adds two numbers."""
    return first_number + second_number

if __name__ == "__main__":
    mcp.run()