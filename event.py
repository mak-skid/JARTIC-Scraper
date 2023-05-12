from sqlalchemy import Column, DateTime, Text, Integer
from dbsetting import Base, ENGINE

class Event(Base):
    """
    Event model
    """

    __tablename__ = "event"
    __table_args__=({"mysql_engine": "InnoDB"})
    time = Column("time", DateTime, nullable=False, primary_key=True)
    area = Column("area", Text, nullable=False)
    cause = Column("cause", Text, nullable=False)
    direction = Column("direction", Text, nullable=False, primary_key=True)
    section = Column("section", Text, nullable=False, primary_key=True)
    route = Column("route", Text, nullable=False)
    detail = Column("detail", Text, nullable=False)
    length = Column("length", Integer, nullable=True)
    coordinates = Column("coordinates", Text, nullable=True)
    

def main():
    Base.metadata.create_all(ENGINE)

if __name__ == "__main__":
    main()