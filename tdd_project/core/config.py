from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )

    PROJECT_NAME: str = 'Store Api'
    ROOT_PATH: str = '/'
    DATABASE_URL: str
    API_V1_STR: str = '/api/v1'


settings = Settings()
