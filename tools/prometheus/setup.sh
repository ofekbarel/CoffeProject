#!/bin/bash

kubectl create ns monitor

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm install prometheus prometheus-community/prometheus --namespace monitor

kubectl get all

kubectl get svc -n monitor prometheus-server

kubectl expose service prometheus-server --type=LoadBalancer --target-port=9090 --name=prometheus-server-ext -n monitor