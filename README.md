# MCP Server Explorations

I am exploring how to build MCP (Model Context Protocol) servers using different approaches and frameworks. This repo contains my experiments and learnings along the way.

## What is MCP?

MCP works like a universal translator between AI assistants and external tools. Instead of creating separate integrations for every app or service, it provides a single standard protocol that connects everything seamlessly.

Think of it this way, instead of teaching claude how to talk to your calculator, weather api and database one by one, you just connect them through MCP, and claude instantly knows how to use them all.

## My Explorations

### Exploration 1: Getting Started with FastMCP

I started with the basics using FastMCP, building a simple calculator server in two ways:

- **`fastmcp_calci.py`** - My first attempt. A basic STDIO based server with multiply, divide, add and subtract operations. I learned how to use tool decorators and customize descriptions.
- **`fastmcp_calciV2.py`** - In this file, I switched to http from stdio, this version is easier to test with MCP inspector.

### Exploration 2: Combining FastAPI with MCP

**`fastapi_mcp_calci.py`** - Here i explored a different angle, what if we already have a REST API? Turns out we can convert it to an MCP server pretty easily with `fastapi-mcp`. Our API endpoints automatically become tools that AI can use.

### Exploration 3: RSS Feed Reader

**Coming soon** - Moving beyond calculators to something more practical. This will be a very basic MCP server that reads RSS feeds so AI assistants can fetch and analyze real time content from websites.

## What i have Learned So Far

The same functionality can be exposed in different ways depending on what you need:

- **STDIO** perfect for local tools, best for development and testing purposes
- **HTTP** makes testing easier and works for remote access, great for deployment
- **FastAPI integration** is great when we want both a REST API and MCP tools from one codebase

## Try It Out

```bash
# install requirements
pip install fastmcp fastapi fastapi-mcp uvicorn[standard]

# run any of the explorations
python exploration1/fastmcp_calci.py
python exploration1/fastmcp_calciV2.py
python exploration2/fastapi_mcp_calci.py

# want to see what is happening? use MCP inspector
npx @modelcontextprotocol/inspector python exploration1/fastmcp_calci.py

# run this command (replace <port-num> with your actual port) to connect to an HTTP based MCP server
npx @modelcontextprotocol/inspector http://localhost:<port-num>/mcp 
```

---

*Just me learning about MCP by building things with it.*