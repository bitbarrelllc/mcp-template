from .server import MCPServer
from .config import ServerSettings


def create_mcp_server(settings: ServerSettings, **kwargs) -> MCPServer:
    """
    Create and configure the MCP server.
    """
    mcp_server = MCPServer(settings, **kwargs)
    return mcp_server