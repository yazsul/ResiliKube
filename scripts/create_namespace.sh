#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <namespace>"
  exit 1
fi

NAMESPACE=$1

kubectl create namespace $NAMESPACE
if [ $? -ne 0 ]; then
  echo "Failed to create namespace $NAMESPACE"
  exit 1
fi

echo "Namespace $NAMESPACE created successfully."
