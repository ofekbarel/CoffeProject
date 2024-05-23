#!/bin/bash

kubectl create ns monitor

helm repo add grafana https://grafana.github.io/helm-charts

helm repo update

helm install grafana grafana/grafana --namespace monitor

kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-ext -n monitor

kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo