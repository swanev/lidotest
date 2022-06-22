TESTS:
=========

Usage:
----------------

*** Check Docker daemon access with TCP and containers status: ***

python3 docker_check.py FQDN_OR_IP_ADDRES_OF_DOCKER_NODE PORT

*** Check services accessability: ***

python3 services_check.py FQDN_OR_IP_ADDRES_OF_DOCKER_NODE PORT1 PORT2 PORT3 ...

Example:
----------------

***Docker containers check and access docker daemon with TCP:***

python3 docker_check.py 192.168.122.201 2375

python3 services_check.py 192.168.122.201 9100 3000 9092 9081 9093 9090 3100

***For down and up containers:***

ansible-playbook --user YOUR_USER_NAME --inventory YOUR_INVENTORY_FILE deploy-monitoring.yml --tags remove,start
