import asyncio
import os
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Setup paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    server_path = os.path.abspath(os.path.join(current_dir, "..", "server", "server.py"))

    # Define connection using the current Python executable
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[server_path],
        env=None
    )

    print("🚀 Connecting to Lightweight Code Gen Server...")

    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                print("\n--- Model is ready (DeepSeek-Coder 1.3B) ---")
                user_prompt = input("📝 What should I code? ")
                
                # Call the generator tool
                result = await session.call_tool(
                    "generate_code", 
                    arguments={"prompt": user_prompt}
                )

                print("\n" + "="*40)
                print(result.content[0].text)
                print("="*40)

    except Exception as e:
        print(f"\n❌ Client Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())