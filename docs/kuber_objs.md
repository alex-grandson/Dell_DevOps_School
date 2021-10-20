# Основные объекты Kubernetes

## 1. Pod
- объект, в котором работают 1 или больше контейнеров.

## 2. Deployment
- множество одинаковых pods
- нужен для auto scaling и для обновления Container Image
- держит минимальное количество работающих pods

# 3. Service
- предоставляет доступ к Deployment через
  - ClusterIP
  - NodePort
  - LoadBalancer
  - ExternalName

# 4. Nodes
- сервера, где все работает

# 5. Cluster
- логическое обхединение Nodes
- 