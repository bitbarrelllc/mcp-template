import os
from enum import Enum

from pydantic_settings import BaseSettings
from starlette.config import Config

from .enums import EnvironmentOption, ServerTransportOptions

config = Config(".env")


class ServerSettings(BaseSettings):
    SERVER_NAME: str = config("SERVER_NAME", default="MCP Server")
    SERVER_INSTRUCTIONS: str | None = config("SERVER_INSTRUCTIONS", default="MCP Server Project Template")
    SERVER_TRANSPORT: ServerTransportOptions | None = config("SERVER_TRANSPORT", default=ServerTransportOptions.STDIO.value)


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: EnvironmentOption = config("ENVIRONMENT", default=EnvironmentOption.LOCAL)


class Settings(
    ServerSettings,
    EnvironmentSettings,
):
    pass


settings = Settings()