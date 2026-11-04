from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # se leen de las variables de entorno (TRD §4.4); en Docker llegan por el env_file del compose
    app_env: Literal["dev", "test", "prod"]
    database_url: str
    log_level: str = "INFO"


settings = Settings()
