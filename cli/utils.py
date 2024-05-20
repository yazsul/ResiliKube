import os

def load_config():
    config = {}
    with open(os.path.join(os.path.dirname(__file__), '../config/config.properties')) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                name, value = line.split('=')
                config[name.strip()] = value.strip()
    return config

def get_bash_path():
    config = load_config()
    return config.get('git_bash_path', 'bash')
