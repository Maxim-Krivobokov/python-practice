# JSON 
cross-language format

to process datetime properly, we should decode json-data (type = bytes object) to string, 
and convert string with datetime.fromisoformat func

json.loads = for bytes
json.dumps = for strings
