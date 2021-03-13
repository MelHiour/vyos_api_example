import helpers
import click
import constants

@click.command()
@click.option('--inventory_file', '-i', required=True, help='Inventory YAML')
@click.option('--deployment_file', '-d', required=True, help='Deployment YAML')
@click.option('--api_key', '-a', required=True, help='API key name from constants.py')
def main(inventory_file, deployment_file, api_key):
    key = getattr(constants, api_key)
    print('API key gathered')

    inventory = helpers.parse_yaml(inventory_file)
    print('Inventory file "{}" parsed.'.format(inventory_file))

    deployment = helpers.parse_yaml("deployments/" + deployment_file)
    print('Deployment file "{}" parsed.'.format(deployment_file))

    for device, details in deployment.items():
        generated_config = helpers.generate_cfg_from_template("templates/" + details['template'], details['data'])
        print('\tConfig for "{}" generated.'.format(device))

        prepared_config = helpers.prep_config(generated_config, key)
        print('\tConfig prepared.')
        
        print('\tPushing config to "{}"'.format(device))
        r = helpers.post_config(inventory[device]['address'], prepared_config)
        
        print('\tReturned result is "{}"'.format(r.text))
        
        print('\tSaving configuration...')
        r = helpers.save_config(inventory[device]['address'], key)
        print('\tReturned result is "{}"'.format(r.text))

if __name__ == '__main__':
    main()
