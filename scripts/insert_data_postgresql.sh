#!/bin/bash

POD_NAME=$(kubectl get pods -n app -l app=postgres -o jsonpath="{.items[0].metadata.name}")
kubectl exec -it $POD_NAME -n app -- psql -U testuser -d testdb -c "CREATE TABLE test_table (id SERIAL PRIMARY KEY, value TEXT); INSERT INTO test_table (value) VALUES ('Test data');"

if [ $? -ne 0 ]; then
  echo "Failed to insert data into PostgreSQL"
  exit 1
fi

echo "Data inserted into PostgreSQL successfully."
