import yaml
import json
import jsonschema

def main():
    with open('docker_daemon.yaml', 'r') as yaml_file:
        yaml_conf = yaml.safe_load(yaml_file)
    print(yaml_conf)

    with open('docker_daemon.schema.json', 'r') as schema_file:
        schema = json.load(schema_file)

    print(jsonschema.validate(instance=yaml_conf, schema=schema))

    with open('docker_daemon_new.json', 'w') as json_out:
        json.dump(yaml_conf, json_out, indent=4)

    with open("docker_daemon_new.yaml", 'w') as yaml_out:
        yaml.safe_dump(yaml_conf, yaml_out)

    return


if __name__ == '__main__':
    main()