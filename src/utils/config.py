import json

def get_base_url():
    with open("..\config\config.json", "r") as config_file:
        config = json.load(config_file)
        return config.get("base_url", "https://example.com")  # Default URL if not found
