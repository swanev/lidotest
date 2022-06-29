Monitoring:
=========

Deploy Grafana/Prometheus/AlertManager/Loki/node-exporter/cadvisor/Promtail with Prometheus docker_sd_config for Docker service descovery.

Requirements:
------------
community.docker.(docker_plugin, docker_compose)
community.grafana.(grafana_dashboard, grafana_datasource)

Linux, Docker/Podman

Role Variables:
--------------

# common
log_driver

# loki
loki_docker_image
loki_docker_ports
loki_listen_port
loki_grpc_port
alertmanager_url
loki_docker_net
loki_docker_log_dir

# promtail
promtail_docker_image
promtail_docker_ports
promtail_docker_net
promtail_listen_port
promtail_docker_data_dir
promtail_docker_conf_dir
promtail_docker_log_dir
loki_url

# grafana
grafana_docker_image
grafana_docker_conf_dir
grafana_docker_log_dir
grafana_docker_ports
grafana_docker_data_dir
grafana_admin
grafana_password

# node-exporter
node_exporter_image
node_exporter_file_dir
node_exporter_docker_ports

# alertmanager
alertmanager_image
alertmanager_conf_dir
alertmanager_data_dir
alertmanager_docker_ports
alertmanager_listen_port

# cadvisor
cadvisor_docker_image
cadvisor_docker_ports


Dependencies
------------
community.docker.(docker_plugin, docker_compose)
community.grafana.(grafana_dashboard, grafana_datasource)

Role tags:
--------------

**install** - For first time installation procedure.

**install-loki-plugin** - Run installation of Loki plugin for Docker. Included in "install" and "never" tags. 

**uninstall-loki-plugin** - Uninstall Loki plugin for DOcker. Included to "never" tags.

**docker-daemon** - Run task to reconfigure Docker daemon to grant access for Prometheus.

**prepare_dirs** - Create dirs for which will be mounted to containers. Included in "install" tag.

**upgrade** - Run task when you need to upgrade configs and relaunch containers. Included in "install" tag.

**start** - Just run docker-compose up -d. Included in "install" tag.

**remove** - Just run docker-compose down

Example Playbook:
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

***For first time installation run:***

ansible-playbook --user YOUR_USER_NAME --inventory YOUR_INVENTORY_FILE deploy-monitoring.yml --tags install --extra-vars="grafana_admin=YOUR_USER grafana_password=YOUR_PASSWORD"

***For upgrade configs/dashboards:***

ansible-playbook --user YOUR_USER_NAME --inventory YOUR_INVENTORY_FILE deploy-monitoring.yml --tags upgrade --extra-vars="grafana_admin=YOUR_USER grafana_password=YOUR_PASSWORD"
