A simple script to test VyOS API capabilities.
Documentation can be found here https://docs.vyos.io/en/latest/automation/vyos-api.html#vyosapi

## Files
```
├── constants.py                  Place you API key here
├── deployments                   
│   └── deploy_new_client.yaml    Deployment file
├── helpers.py                    Some scripts...
├── inventory.yaml                Hostanames and IP addresses
├── requirements.txt              All you need to run it
├── templates                     Add your templates here
│   ├── new_client_fw.j2
│   └── new_client_rtr.j2
└── vyos_deploy.py                The script itself
```

#### Execution example
```
# python3 vyos_deploy.py -i inventory.yaml -d deploy_new_client.yaml -a API_KEY
API key gathered
Inventory file "inventory.yaml" parsed.
Deployment file "deploy_new_client.yaml" parsed.
	Config for "R1" generated.
	Config prepared.
	Pushing config to "R1"
	Returned result is "{"success": true, "data": null, "error": null}"
	Saving configuration...
	Returned result is "{"success": true, "data": "Saving configuration to '/config/config.boot'...\nDone\n", "error": null}"

	Config for "R2" generated.
	Config prepared.
	Pushing config to "R2"
	Returned result is "{"success": true, "data": null, "error": null}"
	Saving configuration...
	Returned result is "{"success": true, "data": "Saving configuration to '/config/config.boot'...\nDone\n", "error": null}"

	Config for "F1" generated.
	Config prepared.
	Pushing config to "F1"
	Returned result is "{"success": true, "data": null, "error": null}"
	Saving configuration...
	Returned result is "{"success": true, "data": "Saving configuration to '/config/config.boot'...\nDone\n", "error": null}"

	Config for "F2" generated.
	Config prepared.
	Pushing config to "F2"
	Returned result is "{"success": true, "data": null, "error": null}"
	Saving configuration...
	Returned result is "{"success": true, "data": "Saving configuration to '/config/config.boot'...\nDone\n", "error": null}"


```
