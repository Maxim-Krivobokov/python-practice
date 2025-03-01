import kubernetes as k8s


class Environment:
    application = "testenv"

    # here Custom resource is created
    def __init__(self, name, port, env_type, image):
        self._port = port
        self._env_type = env_type
        self._image = image

        # definition of metadata
        metadata = k8s.client.V1ObjectMeta(name=name,
                                           labels={
                                               "application": self.application,
                                               "type": self._env_type
                                           })
        # definition of pods
        spec = k8s.client.V1PodSpec(
            containers=k8s.client.V1Container(image=self._image,
                                                name=name,
                                                ports=[
                                                    k8s.client.V1ContainerPort(
                                                        container_port=port
                                                    )
                                                ],
                                                image_pull_policy='IfNotPresent')
        )
        #definition of a pod
        self._pod = k8s.client.V1Pod(
            api_version="v1",
            metadata=metadata,
            spec=spec
        )
        self._svc = {
            "apiVersion": "v1",
            "metadata": {"name": name, "labels": {"application": self.application,
                                                       "type": self._env_type}},
            "spec": {
                "selector": {"application": self.application, "type": self._env_type},
                "type": "ClusterIP",
                "ports": [{"port": port, "targetPort": port}]
            }
        }

        self._ingress = {
            "apiVersion": "extensions/v1beta1",
            "kind": "Ingress",
            "metadata": {"name": name, "labels": {"application": self.application,
                                                  "type": self._env_type}},
            "spec": {
                "rules": [{
                    #"host": f"my-app.s{host_user}.edu.slurm.io",
                    "http": {"paths": [{
                        "path": "/testpath",
                        "backend": {"serviceName": name, "servicePort": port}
                    }]}
                }]
            }
        }

    @property
    def pod(self):
        return self._pod

    @property
    def svc(self):
        return self._svc

    @property
    def ingress(self):
        return self._ingress