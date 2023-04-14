from json_asset import scrape

def producer():
    raw_json = scrape('C03')

    events = {}

    for feature in raw_json["features"]:
        events.append(feature["properties"])

    return events