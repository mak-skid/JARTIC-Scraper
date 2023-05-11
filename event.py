from sqlalchemy import Column, DateTime, Text, Integer
from dbsetting import Base, ENGINE

class Event(Base):
    """
    Event model
    """

    __tablename__ = "event"
    __table_args__=({"mysql_engine": "InnoDB"})
    time = Column("time", DateTime, not_null=True)
    area = Column("area", Text, not_null=True)
    cause = Column("cause", Text, not_null=True)
    direction = Column("direction", Text, not_null=True)
    section = Column("section", Text, not_null=True)
    route = Column("route", Text, not_null=True)
    detail = Column("detail", Text, not_null=True)
    length = Column("length", Integer, not_null=False)
    

def main():
    Base.metadata.create_all(ENGINE)

if __name__ == "__main__":
    main()