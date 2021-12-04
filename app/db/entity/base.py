from sqlalchemy.ext.declarative import declarative_base

_Base = declarative_base()


class BaseEntity(_Base):
    __abstract__ = True
    __tablename__: str
