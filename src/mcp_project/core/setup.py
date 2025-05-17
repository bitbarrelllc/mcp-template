from ..servers import v1_mcp


def create_mcp_server(**kwargs):
    """
    Create and configure the MCP server.
    """
    from fastmcp import FastMCP

    mcp_server = FastMCP(**kwargs)
    mcp_server.mount("v1", v1_mcp)

    return mcp_server