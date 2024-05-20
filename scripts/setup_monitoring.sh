#!/bin/bash

# Install Prometheus and Grafana using Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Create namespace for monitoring
kubectl create namespace monitoring

# Install Prometheus
helm install prometheus prometheus-community/prometheus --namespace monitoring

# Install Grafana
helm install grafana grafana/grafana --namespace monitoring

# Get Grafana admin password
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

echo "Prometheus and Grafana setup completed."
