from sqlalchemy import Column, DateTime, PrimaryKeyConstraint, Text, Integer, Float
from dbsetting import Base, ENGINE

class Event(Base):
    """
    Event model
    """
    __tablename__ = "event"
    __table_args__= ({"mysql_engine": "innodb"})
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    time = Column("time", DateTime, nullable=False)
    area = Column("area", Text, nullable=False)
    cause = Column("cause", Text, nullable=False)
    direction = Column("direction", Text, nullable=False)
    section = Column("section", Text, nullable=False)
    route = Column("route", Text, nullable=False)
    detail = Column("detail", Text, nullable=False)
    length = Column("length", Float, nullable=True)
    coordinates = Column("coordinates", Text, nullable=True)

    def __init__(self, time, area, cause, direction, section, route, detail, length, coordinates):
        self.time = time
        self.area = area
        self.cause = cause
        self.direction = direction
        self.section = section
        self.route = route
        self.detail = detail
        self.length = length
        self.coordinates = coordinates
