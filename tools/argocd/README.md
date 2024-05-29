# argo cd ‼️ #

---
## explain :
We deploy the argocd inside our create namespace.
We can access with a load balancer, and finally we can implement the package using the steering wheel.

---   




## script :
#!/bin/bash

kubectl create namespace argocd

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'

kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath='{.data.password}' | base64 -d
