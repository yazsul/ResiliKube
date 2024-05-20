#!/bin/bash

kubectl rollout undo deployment/nginx-deployment --namespace=app
if [ $? -ne 0 ]; then
  echo "Failed to start rollback"
  exit 1
fi

echo "Rollback started successfully."
