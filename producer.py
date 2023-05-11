from scraper import scrape, current_time
from area_dict import area

def producer(): #iterates each area in area_dict and returns a dictionary of all areas
    current_time = current_time()

    all_areas = {}

    for area_code in area.values():
        all_areas[area_code] = json_rearranger(area_code, current_time)
    
    return current_time, all_areas


def json_rearranger(area_code, current_time): #fetch json and rearrange each element with an updated key
    raw_json = scrape(area_code, current_time)

    new_event = {}
    new_events = [] #list of updated JSON of each traffic event

    keys = ['c', 'd', 'i', 'r', 'rd', 'j', 'coordinates']
    new_keys = ['規制原因', '方向', '区間', '路線名', '規制内容', '渋滞長', '位置']

    for feature in raw_json["features"]:
        event = feature["properties"]
        if "geometry" in feature:
            event["coordinates"] = feature["geometry"]["coordinates"]
        for key, element in event.items():
            if key in keys:
                new_key = new_keys[keys.index(key)]
                new_event[new_key] = element
        new_events.append(new_event.copy())

    return new_events