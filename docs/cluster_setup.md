# Создание кластера

## Настройка control-plane (мастер ноды)

```bash 
kubeadm init --pod-network-cidr=10.244.0.0/16
```

Получаем примерно такое:

```bash
kubeadm join 192.168.0.2:6443 --token d2yvt3.fadic3zs751t3li8 \
  --discovery-token-ca-cert-hash sha256:0bfeefc74e843af52ff730d095125b4e9b835ec63cc87c5709c23f63be49ca60
```

```bash
export KUBECONFIG=/etc/kubernetes/admin.conf

vi /etc/environment
    export KUBECONFIG=/etc/kubernetes/admin.conf

```

Устанавливаем [CNI](https://habr.com/ru/company/southbridge/blog/518782/) Flanel

```bash
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

## Настройка worker (рабочей ноды)

1. Втыкаем команду, которую получили на мастер ноде

```bash
kubeadm join 192.168.0.2:6443 --token d2yvt3.fadic3zs751t3li8 \
  --discovery-token-ca-cert-hash sha256:0bfeefc74e843af52ff730d095125b4e9b835ec63cc87c5709c23f63be49ca60
```

2. Радуемся с `kubectl get nodes`


