from pydantic import BaseSettings

from infra.postgres.config_base import PostgresConfigBase


class DBConfig(PostgresConfigBase, BaseSettings):
    class Config:
        env_prefix = "DB_"
