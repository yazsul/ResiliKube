#!/bin/bash

# Load configuration
source $(dirname "$0")/../config/config.properties

# Delete any existing Minikube cluster
minikube delete

echo "Minikube cluster deleted successfully."
