#!/bin/bash

# Check Minikube status
minikube status
if [ $? -ne 0 ]; then
  echo "Minikube is not running. Please start the cluster first."
  exit 1
fi

# Check node status
kubectl get nodes
kubectl describe node minikube

echo "Cluster status is good."
