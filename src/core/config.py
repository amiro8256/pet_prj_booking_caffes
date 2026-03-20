import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
PATH_ENV_FILE = BASE_DIR/"infra"/".env"


class Settings(BaseSettings):
    db_password: str = 'dmin'
    db_user: str = 'postgres'
    db_name: str = 'Test_db'
    db_host: str = 'localhost'
    db_port: str = '5432'
    model_config = SettingsConfigDict(
        env_file=PATH_ENV_FILE, extra="ignore"
    )

    @property
    def DATABASE_URL(self) -> str:
        return (
            f'postgresql+asyncpg://'
            f'{self.db_user}:{self.db_password}@'
            f'{self.db_host}:{self.db_port}/{self.db_name}'
        )

    @property
    def DB_SQLite_URL(self) -> str:
        return 'sqlite+aiosqlite:///./fastapi.db'


settings = Settings()
