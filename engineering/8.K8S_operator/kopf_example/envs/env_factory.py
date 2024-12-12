from env import Environment
import kopf

__envs_conf = {
    'monitoring': (21222, 'monitoring-module:1.0.0')
}

def create_env(env_type, name):
    if env_type in __envs_conf:
        port, image = __envs_conf[env_type]
        # Create environment (pod, svc, ingress) if params are OK (exists in the list)
        return Environment(name, port, env_type, image)
    # most common kopf-related error if something goes wrong
    return kopf.PermanentError(f"Type must be one of {list(__envs_conf.keys())}")