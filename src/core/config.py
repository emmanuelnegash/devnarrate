from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "DevNarrate"
    debug: bool = True

settings = Settings()