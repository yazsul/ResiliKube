import click
from .cluster_initialization import initialize_cluster
from .cluster_cleaning import clean_cluster
from .pod_failure_recovery_test import test_pod_failure_recovery
from .rolling_update_and_rollback import perform_rolling_update_and_rollback
from .persistence_test import test_persistence
from .workflow import run_workflow

@click.group()
def main():
    pass

@main.command()
def init():
    """Initialize the Kubernetes cluster"""
    initialize_cluster()

@main.command()
def clean():
    """Clean the Kubernetes cluster"""
    clean_cluster()

@main.command()
def test_pod_failure():
    """Test pod failure recovery"""
    test_pod_failure_recovery()

@main.command()
@click.argument('experiment')
def workflow(experiment):
    """Run the specified experiment workflow"""
    run_workflow(experiment)

@main.command()
def rolling_update_and_rollback():
    """Perform rolling updates and rollback"""
    perform_rolling_update_and_rollback()

@main.command()
def test_persistence():
    """Test persistence of data with PVC and PostgreSQL"""
    test_persistence()

if __name__ == "__main__":
    main()
