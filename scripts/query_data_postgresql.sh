#!/bin/bash

POD_NAME=$(kubectl get pods -n app -l app=postgres -o jsonpath="{.items[0].metadata.name}")
kubectl exec -it $POD_NAME -n app -- psql -U testuser -d testdb -c "SELECT * FROM test_table;"

if [ $? -ne 0 ]; then
  echo "Failed to query data from PostgreSQL"
  exit 1
fi

echo "Data queried from PostgreSQL successfully."
