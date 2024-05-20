#!/bin/bash

# Load configuration
source $(dirname "$0")/../config/config.properties

# Validate input
if [ -z "$1" ]; then
  echo "Usage: $0 <fault-type>"
  exit 1
fi

FAULT_TYPE=$1
CONFIG_FILE=""

case $FAULT_TYPE in
  pod-failure)
    CONFIG_FILE="../chaos-mesh/pod-failure.yaml"
    ;;
  network-partition)
    CONFIG_FILE="../chaos-mesh/network-partition.yaml"
    ;;
  *)
    echo "Unsupported fault type: $FAULT_TYPE"
    exit 1
    ;;
esac

# Inject fault using Chaos Mesh
kubectl apply -f $CONFIG_FILE
if [ $? -ne 0 ]; then
  echo "Failed to apply Chaos Mesh configuration."
  exit 1
fi

echo "$FAULT_TYPE fault injected successfully."
