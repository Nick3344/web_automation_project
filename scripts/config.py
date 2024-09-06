import json

with open('data/config.json') as config_file:
    config = json.load(config_file)

driver.get(config['base_url'])
username_field.send_keys(config['username'])
password_field.send_keys(config['password'])
