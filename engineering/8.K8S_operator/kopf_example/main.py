import kopf
import kubernetes as k8s
from envs.env_factory import create_env

RESOURCE_GROUP = "slurm.io"
RESOURCE_VERSION = "v1"
RESOURCE_TYPE = "testenv"

@kopf.on.create(RESOURCE_GROUP, RESOURCE_VERSION, RESOURCE_TYPE)
def create_custom_resource(body, spec, logger, **kwargs):
    name = body['metadata']['name']
    env = create_env(spec['type'], name)
    create_k8s_object(spec['namespace'], env, logger)

# func for creating certain resources
def create_k8s_object(namespace, env, logger):
    # different apis for different types of resources
    api = k8s.client.CoreV1Api()
    network_api = k8s.client.NetworkingV1Api()

    # check and create namespace if not exists
    if not any(cluster_ns.metadata.name == namespace for cluster_ns in api.list_namespace().items()):
        logger.info(f"{namespace} not found, going to create it")
        api.create_namespace(k8s.client.V1Namespace(
            metadata=k8s.client.V1ObjectMeta(
                name=namespace
            )
        ))

    # create_namespaced_pood is an enternal k8s api method
    pod = api.create_namespaced_pod(namespace, env.pod)
    logger.info(f"Pod {pod.metadta.name} created")

    svc = api.create_namespaced_service(namespace, env.svc)
    logger.info(f"Service for {pod.metadta.name} created")

    ingress = network_api.create_namespaced_ingress(namespace, env.ingress)
    logger.info(f"Ingress for {pod.metadata.name} created")
