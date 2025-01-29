from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath

from loguru import logger


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='config/.env',
                                      env_file_encoding='utf-8',)
    model_path: DirectoryPath
    model_name: str
    log_filename: str
    log_level: str


settings = Settings()
logger.add(settings.log_filename,
           level=settings.log_level,)

