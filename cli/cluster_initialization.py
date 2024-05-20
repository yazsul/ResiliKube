import os
import subprocess
from .utils import get_bash_path

def initialize_cluster():
    script_path = os.path.abspath("../scripts/initialize_cluster.sh")
    bash_path = get_bash_path()
    subprocess.run([bash_path, script_path], check=True)
    print("Minikube cluster initialized successfully.")
