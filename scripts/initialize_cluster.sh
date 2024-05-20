#!/bin/bash

# Load configuration
source $(dirname "$0")/../config/config.properties

# Delete any existing Minikube cluster
minikube delete

# Set Minikube configurations
minikube config set memory $memory
minikube config set cpus $cpus
minikube config set disk-size $disk_size

# Start Minikube
minikube start --driver=$driver --no-vtx-check
if [ $? -ne 0 ]; then
  echo "Failed to start Minikube with driver $driver. Attempting to start with default driver."
  minikube start
  if [ $? -ne 0 ]; then
    echo "Failed to start Minikube. Check logs for more details."
    exit 1
  fi
fi

echo "Minikube cluster initialized successfully."
