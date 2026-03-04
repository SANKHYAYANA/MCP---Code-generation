from mcp.server.fastmcp import FastMCP
import ollama
import os

# Create the MCP Server
mcp = FastMCP("Code-Generator")

@mcp.tool()
def generate_code(prompt: str, language: str = "python") -> str:
    """
    Generates code using a lightweight model to fit in available RAM.
    """
    try:
        # Using deepseek-coder:1.3b which only needs ~1.5GB of RAM
        response = ollama.chat(
            model='deepseek-coder:1.3b', 
            messages=[
                {
                    'role': 'system', 
                    'content': f"You are a helpful {language} programmer. Return ONLY code. No markdown."
                },
                {
                    'role': 'user', 
                    'content': f"Write {language} code for: {prompt}"
                }
            ]
        )

        code_result = response['message']['content'].strip()
        return f"\n--- GENERATED CODE ---\n\n{code_result}"

    except Exception as e:
        return f"❌ Server Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()