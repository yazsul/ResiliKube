# ResiliKube

ResiliKube is a lightweight framework for automating fault tolerance testing in Kubernetes. It provides a CLI implemented in Python and uses shell scripts for direct cluster operations.

## Project Structure
```ResiliKube/
├── cli/
│ ├── init.py
│ ├── main.py
│ ├── cluster_initialization.py
│ ├── cluster_cleaning.py
│ ├── pod_failure_recovery_test.py
│ ├── rolling_update_and_rollback.py
│ ├── workflow.py
│ └── utils.py
├── chaos-mesh/
│ ├── pod-failure.yaml
│ ├── network-partition.yaml
├── config/
│ └── config.properties
├── scripts/
│ ├── check_status.sh
│ ├── initialize_cluster.sh
│ ├── setup_chaos_mesh.sh
│ ├── setup_monitoring.sh
│ ├── inject_fault.sh
│ ├── create_namespace.sh
│ ├── deploy_nginx.sh
│ ├── start_rollout.sh
│ ├── start_rollback.sh
├── setup.py
└── README.md
```

## Installation

### Requirements

- Python 3.x
- Minikube
- kubectl
- Helm
- Git Bash (for running shell scripts on Windows)

### Install ResiliKube
```sh
pip install -e .
```

## Usage

### Initialize Cluster

```sh
reskube init
```

### Clean Cluster

```
reskube clean
```

### Test Pod Failure Recovery

```
reskube test_pod_failure
```

### Perform Rolling Update and Rollback

```
reskube rolling_update_and_rollback
```

### Run Workflow

```
reskube workflow pod-failure 
reskube workflow rolling-update-and-rollback
```

### Setup Chaos Mesh

```
bash scripts/setup_chaos_mesh.sh
```

### Setup Monitoring (Prometheus and Grafana)

```
bash scripts/setup_monitoring.sh
```

### Check Cluster Status

```
bash scripts/check_status.sh
```

### Configuration
Update the config/config.properties file to configure Minikube and Git Bash (if on Windows)

## Experiment Workflows

### Pod Failure Experiment

1. Run the experiment workflow:

```
reskube workflow pod-failure
```

2. Observe the results in Grafana (http://localhost:3000) and the NGINX logs.

### Rolling Updates and Rollback Experiment

1. Run the experiment workflow:

```
reskube workflow rolling-update-and-rollback
```

2. Observe the results in Grafana (http://localhost:3000) and the NGINX logs.

### Persistence Experiment

1. Run the experiment workflow:

```
reskube workflow persistence
```

2. Observe the results in Grafana (http://localhost:3000) and query data from PostgreSQL to check persistence.
