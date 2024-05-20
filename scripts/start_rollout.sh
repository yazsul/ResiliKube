#!/bin/bash

kubectl set image deployment/nginx-deployment nginx=nginx:latest --namespace=app
if [ $? -ne 0 ]; then
  echo "Failed to start rollout"
  exit 1
fi

echo "Rollout started successfully."
