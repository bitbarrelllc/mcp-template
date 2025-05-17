from ..servers import v1_mcp
from .config import ServerSettings
from .enums import EnvironmentOption, ServerTransportOptions

class MCPServer:
    def __init__(self, settings: ServerSettings, **kwargs):
        self.settings = settings
        self.kwargs = kwargs

        self.mcp_server = self._create_mcp_server()

    def _create_mcp_server(self):
        """
        Create and configure the MCP server.
        """
        from fastmcp import FastMCP

        if isinstance(self.settings, ServerSettings):
            to_update = {
                "name": self.settings.server.name,
                "instructions": self.settings.server.instructions
            }
            self.kwargs.update(to_update)

        # TODO: Add Auth middleware when in PRODUCTION
        mcp_server = FastMCP(**self.kwargs)
        mcp_server.mount("v1", v1_mcp)

        return mcp_server

    async def serve(self):
        """
        Start the MCP server.
        """
        if isinstance(self.settings, ServerSettings):
            if self.settings.environment == EnvironmentOption.PRODUCTION:
                transport = ServerTransportOptions.STREAMABLE_HTTP.value
            else:
                transport = self.settings.server.transport.value
            # Use serve() in async contexts
            await self.mcp_server.run_async(transport=transport)