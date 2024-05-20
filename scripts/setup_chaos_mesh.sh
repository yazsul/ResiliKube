#!/bin/bash

# Add Chaos Mesh repository
helm repo add chaos-mesh https://charts.chaos-mesh.org
helm repo update

# Install Chaos Mesh
kubectl create namespace chaos-testing
helm install chaos-mesh chaos-mesh/chaos-mesh --namespace=chaos-testing

echo "Chaos Mesh setup completed."
