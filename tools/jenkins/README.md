# Jenkins 📝


## Explain :
We will deploy jenkins inside namescpae named jenkins, this tool will be used for the CI process.
during which we will run tests for our application and using pytest, we will make a merge request, and if the branch is main we will also build a docker image and push it to dockeruhb


---
## script :


#!/bin/bash

kubectl create ns jenkins

helm repo add jenkins https://charts.jenkins.io

helm repo update

helm upgrade --install myjenkins jenkins/jenkins -n jenkins

kubectl get secret -n jenkins myjenkins -o jsonpath="{.data.jenkins-admin-password}" | base64 --decode

kubectl expose service myjenkins --type=LoadBalancer --target-port=8080 --name=jenkins-ext -n jenkins
