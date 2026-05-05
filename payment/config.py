from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    inventory_url: str
    redis_host: str
    redis_port: int

    class Config:
        env_file = ".env"

settings = Settings()