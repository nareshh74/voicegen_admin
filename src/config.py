# 3rd party modules
from pydantic import BaseSettings
import pyodbc


class AppConfig(BaseSettings):
    host: str
    port: int
    db_connection_string: str
    debug: bool
    gpu_host: str
    gpu_username: str
    gpu_password: str
    
    class Config:
        env_file = ".env"


config = AppConfig()
