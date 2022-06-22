import docker
import sys
from colorama import Fore, Style
IP_PORT="tcp://"+sys.argv[1]+":"+sys.argv[2]
DOCKER_CLIENT = docker.DockerClient(base_url=IP_PORT)
RUNNING = 'running'
containers = ("grafana","cadvisor","prometheus","node-exporter","loki","alertmanager","promtail")

def is_running(container_name):
    """
    verify the status of a sniffer container by it's name
    :param container_name: the name of the container
    :return: Boolean if the status is ok
    """
    container = DOCKER_CLIENT.containers.get(container_name)

    container_state = container.attrs['State']

    container_is_running = container_state['Status'] == RUNNING

    return container_is_running

try:
   DOCKER_CLIENT

except:
   print(Fore.RED + "Docker daemon unaccessable")

else:
   print(Fore.GREEN + "Docker daemon accessable with TCP")
   print()
   my_container_name = "grafana"
   for container in containers:
       if is_running(container) is True:
          print(Fore.GREEN + "The container",container.upper(),"is RUNNINg:",is_running(container))
          print()
       else:
          print(Fore.RED + "The container",container.upper(),"is NOT RUNNINg:", is_running(container))
