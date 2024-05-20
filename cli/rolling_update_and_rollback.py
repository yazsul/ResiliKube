import subprocess
from .utils import get_bash_path

def perform_rolling_update_and_rollback():
    bash_path = get_bash_path()
    
    print("Starting rollout of NGINX deployment...")
    subprocess.run([bash_path, "../scripts/start_rollout.sh"], check=True)
    
    print("Injecting failure during rollout...")
    subprocess.run([bash_path, "../scripts/inject_fault.sh", "pod-failure"], check=True)
    
    print("Starting rollback of NGINX deployment...")
    subprocess.run([bash_path, "../scripts/start_rollback.sh"], check=True)
    
    print("Rolling update and rollback experiment completed.")
