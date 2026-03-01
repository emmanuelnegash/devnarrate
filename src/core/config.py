from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "DevNarrate"
    debug: bool = False

    # Used in src/main.py lifespan() to optionally create tables in dev/test
    db_auto_create_tables: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
    )


settings = Settings()