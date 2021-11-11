# NGINX Ingress Controller setup

## Настройка ролей нод

```
kubectl label node k8s-worker1.dmosk.local node-role.kubernetes.io/worker=worker
kubectl label node k8s-worker2.dmosk.local node-role.kubernetes.io/worker=worker
```

```
kubectl get nodes               
                                                
NAME                      STATUS   ROLES                  AGE   VERSION
k8s-master1.dmosk.local   Ready    control-plane,master   46h   v1.22.3
k8s-worker1.dmosk.local   Ready    worker                 46h   v1.22.3
k8s-worker2.dmosk.local   Ready    worker                 46h   v1.22.3
```

## Установка Helm

...

## Установка ingress контроллера

1. Добавить репозиторий 

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
```

2. Распакуем чарт и перейдем туда

```bash
helm pull ingress-nginx/ingress-nginx --untar
cd ingress-nginx/
```
3. Будем править `values.yaml` как нам хочется

- Пропишем, что хотим запускать ingress только на воркер нодах
```yaml
nodeSelector:
    kubernetes.io/os: "linux"
    node-role.kubernetes.io/worker: "true"
```

- Хотим две реплики для двух нод
```yaml
  replicaCount: 2

  minAvailable: 1
```

- Для того, чтобы реплики ingress запускались на разных нодах (что важно для отказостойчивости), раскомментируем вот эти строчки
```yaml
  ## Affinity and anti-affinity
  ## Ref: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity

  affinity: 
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: app.kubernetes.io/name
              operator: In
              values:
              - ingress-nginx
            - key: app.kubernetes.io/instance
              operator: In
              values:
              - ingress-nginx
            - key: app.kubernetes.io/component
              operator: In
              values:
              - controller
          topologyKey: kubernetes.io/hostname
```

4. Непосредственно установка

```yaml
helm install ing-control ingress-nginx
```

Output:

```yaml
NAME: ing-control
LAST DEPLOYED: Wed Nov 10 23:22:50 2021
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
The ingress-nginx controller has been installed.
It may take a few minutes for the LoadBalancer IP to be available.
You can watch the status by running 'kubectl --namespace default get services -o wide -w ing-control-ingress-nginx-controller'

An example Ingress that makes use of the controller:

  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    annotations:
      kubernetes.io/ingress.class: nginx
    name: example
    namespace: foo
  spec:
    ingressClassName: example-class
    rules:
      - host: www.example.com
        http:
          paths:
            - path: /
              pathType: Prefix
              backend:
                service:
                  name: exampleService
                  port: 80
    # This section is only required if TLS is to be enabled for the Ingress
    tls:
      - hosts:
        - www.example.com
        secretName: example-tls

If TLS is enabled for the Ingress, a Secret containing the certificate and key must also be provided:

  apiVersion: v1
  kind: Secret
  metadata:
    name: example-tls
    namespace: foo
  data:
    tls.crt: <base64 encoded cert>
    tls.key: <base64 encoded key>
  type: kubernetes.io/tls
```

