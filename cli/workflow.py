import subprocess
from .utils import get_bash_path

def run_workflow(experiment):
    bash_path = get_bash_path()
    
    # Step 1: Initialize Cluster
    print("Initializing Minikube cluster...")
    subprocess.run([bash_path, "../scripts/initialize_cluster.sh"], check=True)

    # Step 2: Setup Monitoring and Chaos Mesh
    print("Setting up Prometheus and Grafana for monitoring...")
    subprocess.run([bash_path, "../scripts/setup_monitoring.sh"], check=True)
    print("Setting up Chaos Mesh...")
    subprocess.run([bash_path, "../scripts/setup_chaos_mesh.sh"], check=True)

    # Step 3: Provide Monitoring Access Details
    print("Setting up port forwarding for Grafana...")
    grafana_forward = subprocess.Popen([bash_path, "-c", "kubectl port-forward --namespace monitoring svc/grafana 3000:80"], stdout=subprocess.PIPE)
    print("You can access Grafana at http://localhost:3000")
    print("Use the username 'admin' and the password retrieved from the setup_monitoring.sh script.")

    # Step 4: Create Namespace and Deploy NGINX
    print("Creating 'app' namespace...")
    subprocess.run([bash_path, "../scripts/create_namespace.sh", "app"], check=True)
    print("Deploying NGINX in 'app' namespace...")
    subprocess.run([bash_path, "../scripts/deploy_nginx.sh"], check=True)

    # Step 5: Apply Chaos Experiment
    if experiment == "pod-failure":
        print("Injecting pod failure using Chaos Mesh...")
        subprocess.run([bash_path, "../scripts/inject_fault.sh", "pod-failure"], check=True)
    elif experiment == "rolling-update-and-rollback":
        print("Starting rolling update and rollback experiment...")
        subprocess.run([bash_path, "../scripts/start_rollout.sh"], check=True)
        subprocess.run([bash_path, "../scripts/inject_fault.sh", "pod-failure"], check=True)
        subprocess.run([bash_path, "../scripts/start_rollback.sh"], check=True)
    elif experiment == "persistence":
        print("Running persistence test workflow...")
        subprocess.run([bash_path, "../scripts/deploy_postgresql.sh"], check=True)
        subprocess.run([bash_path, "../scripts/insert_data_postgresql.sh"], check=True)
        subprocess.run([bash_path, "../scripts/inject_fault.sh", "pod-failure"], check=True)
        subprocess.run([bash_path, "../scripts/query_data_postgresql.sh"], check=True)
    else:
        print(f"Unknown experiment: {experiment}")
        return

    # Step 6: Provide Logs and Instructions
    print("Monitoring logs for NGINX pod...")
    nginx_logs = subprocess.Popen([bash_path, "-c", "kubectl logs -n app -l app=nginx -f"], stdout=subprocess.PIPE)

    # Step 7: Clean and Terminate Cluster
    input("Press Enter to clean and terminate the cluster...")
    print("Cleaning Minikube cluster...")
    subprocess.run([bash_path, "../scripts/initialize_cluster.sh"], check=True)
    print("Minikube cluster cleaned and terminated.")
