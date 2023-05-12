from sqlalchemy.orm import sessionmaker
from dbsetting import ENGINE
from producer import producer
from event import Event

SessionClass = sessionmaker(ENGINE)  # create session class
session = SessionClass()

def insert_event():
    data = producer()

    for index, each_area in enumerate(data[1].values()):
        for each_event in each_area:
            time = data[0]
            area = list(data[1].keys())[index]
            cause = each_event["規制原因"]
            direction = each_event["方向"]
            section = each_event["区間"]
            route = each_event["路線名"]
            detail = each_event["規制内容"]
            length = each_event.get("渋滞長") #used 'get' method to avoid KeyError
            coordinates = each_event.get("位置")

            event = Event(time=time, area=area, cause=cause, direction=direction, section=section, route=route, detail=detail, length=length, coordinates=coordinates)
            session.add(event)
            session.commit()
    
    print('insert_event.py: ' + time)

def select_event(current_time):
    events = session.query(Event).filter(Event.time == current_time).all()
    
    print('select_event.py: ' + current_time)

    return events

insert_event()