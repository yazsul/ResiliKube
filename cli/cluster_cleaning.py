import subprocess
from .utils import get_bash_path

def clean_cluster():
    script_path = "../scripts/initialize_cluster.sh"
    bash_path = get_bash_path()
    subprocess.run([bash_path, script_path], check=True)
    print("Minikube cluster cleaned successfully.")
