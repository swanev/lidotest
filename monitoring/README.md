Monitoring
=========

Deploy Grafana/Prometheus/AlertManager/Loki/node-exporter/cadvisor

Requirements
------------

Linux, Docker/Podman

Role Variables
--------------

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

# node-exporter
node_exporter_image
node_exporter_file_dir

# alertmanager
alertmanager_image
alertmanager_conf_dir
alertmanager_data_dir


Dependencies
------------

 

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

ansible-playbook --user user_name --inventory inventory_file deploy-monitoring.yml

    - name: Deploy monitoring
      hosts: monitoring
      become: true
      become_method: sudo
      gather_facts: true
      roles:
         - monitoring         
