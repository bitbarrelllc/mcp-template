from .core.setup import create_mcp_server

mcp_server = create_mcp_server(name="mcp-project", instructions="This is the main MCP server for the project.")

async def serve():
    # Use run_async() in async contexts
    await mcp_server.run_async(transport="streamable-http")

def main():
    import asyncio
    asyncio.run(serve())

if __name__ == "__main__":
    main()