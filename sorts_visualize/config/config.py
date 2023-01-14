import yaml


def read_config():
    with open('sorts_visualize/config/config.yaml') as f:
        return yaml.load(f, Loader=yaml.Loader)
