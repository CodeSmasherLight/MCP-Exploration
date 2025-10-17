from fastmcp import FastMCP

mcp = FastMCP(name="Calculator")


@mcp.tool(name="multiply", description="gives product of two nums") # now instead of docstring, the description within this tool() will be shown on MCP inspector
def multiply(a: float, b: float) -> float:
    """Multiply two numbers
    
    args: a(float)-> first number
          b(float)-> second number

    returns: float -> the product of the two numbers            
    """
    return a * b

@mcp.tool() 
def division(a: float, b: float) -> float:
    """Devide two numbers
    
    args: a(float)-> first number
          b(float)-> second number

    returns: float -> the quotient of the two numbers            
    """
    if b == 0:
        raise ValueError("We cannot divide by zero")
    return a / b

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers
    
    args: a(float) -> first number
          b(float) -> second number

    returns: float -> the sum of the two numbers           
    """
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers
    
    args: a(float)-> first number
          b(float)-> second number

    returns: float -> the difference of two numbers            
    """
    return a - b

if __name__ == "__main__":
    mcp.run() # STDIO by default