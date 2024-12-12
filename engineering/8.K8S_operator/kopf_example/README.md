# Need to install minikube

WSL and minikube - ??? 
Vagrant and ubuntu + minikube

1) launch minikube

2) create manifests

3) test connection to minikube

4) create venv with kopf + kubernetes

5) create main.py, here later main operations with operator would be defined
    - namespace create
    - pod create

6) write environment in envs/env.py
    class Environment with k8s objects
    pods and svcs and ingresses are defined here

7) create env_factory.py
   takes some arguments and creates instance of a class "Environment"

7.5) in main py -add main code (creation of main resources)

8) Operator is defined in Dockerfile

9) Build docker image of operator

10) Build docker image of monitoring module, with name="monitoring-module:1.0.0"
add this name to the env_factory; also add port of the flask app (21222)

11) we can apply all resources with kubectl
  - rbac.yaml
  - crd.yaml
  - service_account.yaml
  - operator_deployment.yaml

12) check that pod in given namespace is created
   - how to check - if execute "kubectl port-forward" then check the localhost port, 
   - we can check the Flask -monitoring-module response in browser