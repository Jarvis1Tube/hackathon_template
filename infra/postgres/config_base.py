from pydantic import BaseModel


class PostgresConfigBase(BaseModel):
    driver: str
    user: str
    password: str
    host: str
    port: str
    database: str

    app_schema: str
    max_connections_count: int
    connection_timeout_secs: int

    @property
    def url(self):
        return (
            f"postgresql+{self.driver}://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
        )
