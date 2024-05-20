import subprocess
from .utils import get_bash_path

def test_pod_failure_recovery():
    script_path = "../scripts/inject_fault.sh"
    bash_path = get_bash_path()
    subprocess.run([bash_path, script_path, "pod-failure"], check=True)
    print("Pod failure recovery test completed.")
