from contextlib import contextmanager
from typing import Iterator

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Connection, Engine
from sqlalchemy.orm import Session

from infra.postgres.config_base import PostgresConfigBase


def _pick_schema_query():
    return text("SET search_path TO :app_schema;")


def get_engine(config: PostgresConfigBase):
    return create_engine(url=config.url)


@contextmanager
def get_connection_ctx(
    engine: Engine,
    config: PostgresConfigBase,
) -> Iterator[Connection]:
    with engine.connect() as connect:
        # May be add if for sqlite case
        with connect.begin():
            connect.execute(_pick_schema_query(), app_schema=config.app_schema)

        yield connect


@contextmanager
def get_session_ctx(engine: Engine, config: PostgresConfigBase) -> Iterator[Session]:
    with get_connection_ctx(engine, config) as connect:
        yield Session(connect)
