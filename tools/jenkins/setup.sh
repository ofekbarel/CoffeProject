#!/bin/bash

kubectl create ns jenkins

helm repo add jenkins https://charts.jenkins.io

helm repo update

helm upgrade --install myjenkins jenkins/jenkins -n jenkins

kubectl get secret -n jenkins myjenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode

kubectl expose service myjenkins --type=LoadBalancer --target-port=8080 --name=jenkins-ext -n jenkins