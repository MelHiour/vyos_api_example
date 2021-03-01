import yaml 
import logging
import requests
import json
import urllib3
from jinja2 import Template
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def parse_yaml(file):   
    '''
    Just parsing yaml and returing the native python object.
    file(str): name of yaml file
    '''
    with open(file) as file:
        result = yaml.load(file, Loader=yaml.FullLoader)
    return(result)

def generate_cfg_from_template(template_file, data_dict): 
    '''
    Just generating a string with template using a data_dict
    '''
    template = Template(open(template_file).read())  
    return(template.render(data_dict)) 

def prep_config(generated_config, api_key):
    '''
    Creating a dictionary which can be accepted by VyOS
    {'data':(None,DATA),{'key':(None,KEY)}
    '''
    to_push = {}
    to_push['data'] = (None, generated_config.replace('\n',''))
    to_push['key'] = (None, api_key)
    return(to_push)

def post_config(target, to_push):
    '''
    Posting data to the target
    '''
    url = 'https://' + target + '/configure'
    r = requests.post(url, files=to_push, verify=False)
    return(r)

