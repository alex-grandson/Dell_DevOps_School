# Создание кластера с ипользованием `kind`

## Установка `KIND`

KIND - Kubernetes in docker.

```bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64 \
    && chmod +x ./kind
sudo mv ./kind /usr/local/bin/
```

## Создание простых двух кластеров

```bash
kind create cluster --name kind-1
```

По окончании можем видеть сообщение об успехе:
```bash
 ✓ Ensuring node image (kindest/node:v1.21.1) 🖼 
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-kind-1"
You can now use your cluster with:

kubectl cluster-info --context kind-kind-1

Have a nice day! 👋
```

Теперь наши кластеры отображаются как ноды:
```bash
~ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                       NAMES
d35a1e68a856   kindest/node:v1.21.1   "/usr/local/bin/entr…"   13 minutes ago   Up 13 minutes   127.0.0.1:41219->6443/tcp   kind-2-control-plane
5fc11f4477ff   kindest/node:v1.21.1   "/usr/local/bin/entr…"   14 minutes ago   Up 14 minutes   127.0.0.1:38447->6443/tcp   kind-1-control-plane
```