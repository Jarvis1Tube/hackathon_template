from typing import Iterator

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Singleton
from sqlalchemy.engine.base import Connection, Engine
from sqlalchemy.orm import Session

from app.config.db import DBConfig
from infra.postgres import connection as postgres
from infra.postgres.config_base import PostgresConfigBase


class DBContainer(DeclarativeContainer):
    db_config: Singleton[PostgresConfigBase] = Singleton(DBConfig, _env_file=".env")
    engine: Singleton[Engine] = Singleton(postgres.get_engine, config=db_config.provided)
    connection: Factory[Iterator[Connection]] = Factory(
        postgres.get_connection_ctx, engine=engine.provided, config=db_config.provided
    )
    session: Factory[Iterator[Session]] = Factory(
        postgres.get_session_ctx, engine=engine.provided, config=db_config.provided
    )
