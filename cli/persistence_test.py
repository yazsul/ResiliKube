import subprocess
from .utils import get_bash_path

def test_persistence():
    bash_path = get_bash_path()

    # Step 1: Deploy PostgreSQL with PVC
    print("Deploying PostgreSQL with PVC...")
    subprocess.run([bash_path, "../scripts/deploy_postgresql.sh"], check=True)

    # Step 2: Insert data into PostgreSQL
    print("Inserting data into PostgreSQL...")
    subprocess.run([bash_path, "../scripts/insert_data_postgresql.sh"], check=True)

    # Step 3: Inject failure using Chaos Mesh
    print("Injecting failure using Chaos Mesh...")
    subprocess.run([bash_path, "../scripts/inject_fault.sh", "pod-failure"], check=True)

    # Step 4: Query data from PostgreSQL
    print("Querying data from PostgreSQL after recovery...")
    subprocess.run([bash_path, "../scripts/query_data_postgresql.sh"], check=True)

    print("Persistence test completed.")
