import json
import jsonschema

def main():
    with open('docker_daemon.broken.json') as json_file:
        my_json = json.load(json_file)

    with open('docker_daemon.schema.json') as json_schema_file:
        schema = json.load(json_schema_file)
    print(my_json)
    print(type(my_json))
    print(schema)
    print(my_json.get("graph", 'empty'))
    print(jsonschema.validate(my_json, schema))


if __name__ == '__main__':
    main()