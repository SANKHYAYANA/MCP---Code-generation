Model Context Protocol: Code Generation Agent
This repository contains an implementation of the Model Context Protocol (MCP) designed for automated code generation. It utilizes a client-server architecture to provide a standardized interface between a local model and a command-line execution environment.

Technical Overview
The system is built to decouple the model execution from the user interface. By using MCP, the server defines specific "tools" that the client can discover and invoke over a persistent connection.

Server Component: Built with FastMCP, the server manages the connection to the Ollama API and handles the logic for code generation.

Client Component: An asynchronous Python application that manages the lifecycle of the server subprocess and provides a stateful interaction loop for the user.

Hardware Optimization: The implementation is configured to use deepseek-coder:1.3b. This allows for high-performance code generation on hardware with limited resources (optimized for systems with 4GB of RAM or less).

mcp-code-generator/
├── server/
│   └── server.py      # FastMCP server defining the generation tools
├── client/
│   └── client.py      # Async client for user interaction and IPC
└── README.md          # Project documentation

Prerequisites
Python 3.10+

Ollama Framework: The Ollama daemon must be running locally.

Model Installation: ollama pull deepseek-coder:1.3b

