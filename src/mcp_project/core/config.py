from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field

from .enums import EnvironmentOption, ServerTransportOptions

class Server(BaseModel):
    name: str = Field(default="MCP Server")
    instructions: str = Field(default="MCP Server Project Template")
    transport: ServerTransportOptions = Field(default=ServerTransportOptions.STDIO)


class ServerSettings(BaseSettings):
    server: Server = Server()
    environment: EnvironmentOption = Field(default=EnvironmentOption.LOCAL)


    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', env_nested_delimiter='__')


settings = ServerSettings()