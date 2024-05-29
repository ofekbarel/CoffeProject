# Prometheus ‼️ 

---
## explain :
We will deploy this tool inside the namespace called monitor.
With this tool we can define different rules for our cluster.

---   




## script :


#!/bin/bash

kubectl create ns monitor

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm install prometheus prometheus-community/prometheus --namespace monitor

kubectl get all

kubectl get svc -n monitor prometheus-server

kubectl patch svc prometheus-server -n monitor -p '{"spec": {"type": "LoadBalancer"}}'
