from scraper import scrape, current_time
from area_dict import area

current_time = current_time()

def producer(): #iterating each area in area_dict and returns a dictionary of all areas
    all_areas = {}

    for area_name in area.values():
        area_code = area[area_name]
        all_areas[area_code] = json_rearranger(area_code)
    
    return current_time, all_areas

def json_rearranger(area_code): #fetch json and rearrange each element with an updated key
    raw_json = scrape(area_code, current_time)

    new_event = {}
    new_events = [] #list of updated JSON of each traffic event

    keys = ['c', 'd', 'i', 'r', 'rd', 'j', 'coordinates']

    for feature in raw_json["features"]:
        event = feature["properties"]
        if feature["geometry"]:
            event["coordinates"] = feature["geometry"]["coordinates"]
        for key, element in event.items():
            if key in keys:
                new_key = ['規制原因', '方向', '区間', '路線名', '規制内容', '渋滞長', "位置"][keys.index(key)]
                new_event[new_key] = element
        new_events.append(new_event)

    return new_events

