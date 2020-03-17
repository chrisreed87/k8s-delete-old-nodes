#!/usr/bin/python3
from kubernetes import client, config

#config.load_kube_config('/var/lib/rancher/k3s/server/cred/admin.kubeconfig')
config.load_kube_config('kubeconfig.yaml')
v1 = client.CoreV1Api()
nodes = v1.list_node(watch=False)

list_of_nodes = []

def delete_node(node):
  name = node
  delete = v1.delete_node(name)
  return delete

for i in nodes.items:
  list_of_nodes.append(i.metadata.name)

for node in list_of_nodes:
  api_response = v1.read_node_status(node)
  for i in api_response.status.conditions:
    if i.type == 'Ready':
        if i.status == 'True':
          print(node + ": Ready")
        else:
          print(node + ": NotReady")
          delete_node(node)