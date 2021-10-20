# Команды

## Minikube

```bash
minikube version
minikube start
minikube stop
minikube delete
minikube ssh

minikube start --cpus=4 --memory=8gb --disk-size=5gb
minikube start -p MY_CLUSTER
```
## Kubectl

```bash
kubectl version
kubectl version --client
kubectl get componentstatuses
kubectl cluster-info
kubectl get nodes
```

# Конфиги

|util|path|
|---|---|
|kubectl|`$USER/.minikube`
|minikube|`$USER/.kubectl`|

# Login на VM с нашим K8s Cluster

Вход под root осуществляется без пароля.

- username: `docker`
- password: `tcuser`

