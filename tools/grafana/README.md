# Grafana 🔆

## Explain :
 We deploy grafana in the namespace called monitor and this tool will be used to display data from our cluster.


---

## script :

#!/bin/bash

kubectl create ns monitor

helm repo add grafana https://grafana.github.io/helm-charts

helm repo update

helm install grafana grafana/grafana --namespace monitor

kubectl patch svc grafana -n monitor -p '{"spec": {"type": "LoadBalancer"}}'

kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
