# Week #4 Docker pipelines

# Week #5: Kubernetes

## Task

Разворачиваем kubernetes кластер на двух виртуальных машинах.

Для ознакомления можем использовать kind: https://kubernetes.io/ru/docs/setup/learning-environment/kind/

Альтернативный способ - playground на официальном сайте kubernetes.

**Definition of done**

- Созданы namespaces;
- Узлы доступны по отношению друг к другу;
- Команда kubectl get nodes выводит доступные узлы в статусе ready.

В финале ждем отчет с инструкцией по установке + финальным выводом консоли.

**Задание со звездочкой**

Написать автоматизацию на Ansible для развертывания k8s.

## Solution

- [Установка и настройка виртуальной машины](install_vm.md)
- [Установка необходимого для Kubernetes](kub_preparation.md)
- Основные понятия