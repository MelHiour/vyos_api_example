import yaml 
import logging
import requests
import json
from constants import API_KEY
from jinja2 import Template

def parse_yaml(file):   
    '''
    Just parsing yaml and returing the native python object.
    file(str): name of yaml file
    '''
    with open(file) as file:
        result = yaml.load(file, Loader=yaml.FullLoader)
    return(result)

def generate_cfg_from_template(template_file, data_dict): 
    template = Template(open(template_file).read())  
    return(template.render(data_dict)) 

def prep_config(generated_config, api_key):
    to_push = {}
    to_push['data'] = (None, generated_config)
    to_push['key'] = (None, api_key)
    return(to_push)

def post_json(target, to_push):
    url = 'http://' + target + '/configure'
    r = requests.post(url, files=to_push, validate=False)
    return(r)

def main(inventory_file, deployment_file):
    inventory = parse_yaml(inventory_file)
    deployment = parse_yaml(deployment_file)
    for device, details in deployment.items():
        json_to_push = generate_cfg_from_template("templates/" + details['template'], details['data'])
        print(json_to_push)
