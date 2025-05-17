from ..servers import v1_mcp
from .config import ServerSettings, EnvironmentSettings
from .enums import EnvironmentOption, ServerTransportOptions

class MCPServer:
    def __init__(self, settings: ServerSettings | EnvironmentSettings, **kwargs):
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
                "name": self.settings.SERVER_NAME,
                "instructions": self.settings.SERVER_INSTRUCTIONS
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
        if isinstance(self.settings, EnvironmentSettings):
            if self.settings.ENVIRONMENT == EnvironmentOption.PRODUCTION:
                transport = ServerTransportOptions.STREAMABLE_HTTP.value
            else:
                transport = self.settings.SERVER_TRANSPORT.value
            # Use serve() in async contexts
            await self.mcp_server.run_async(transport=transport)