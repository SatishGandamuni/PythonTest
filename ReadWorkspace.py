# Import the needed credential and management objects from the libraries.
from azure.identity import AzureCliCredential
from azure.identity import DefaultAzureCredential
from azure.identity import ClientSecretCredential
from azure.mgmt.databricks import AzureDatabricksManagementClient
from azure.mgmt.databricks.models import Sku
from azure.mgmt.databricks.models import WorkspaceCustomBooleanParameter
from azure.mgmt.databricks.models import WorkspaceCustomParameters
from azure.keyvault.secrets import SecretClient

import string
import random
import os
S = 10
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    

from dotenv import load_dotenv
from pathlib import Path
# with open('params.txt') as f:
#     lines = f.readlines()
# print(lines[0])
dotenv_path = Path('./workspace.env')
load_dotenv(dotenv_path=dotenv_path)

credential = DefaultAzureCredential()
client = SecretClient(vault_url="https://pythonkeyvault456.vault.azure.net/", credential=credential)

keyVaultName = "pythonkeyvault456"
KVUri = "https://pythonkeyvault456.vault.azure.net/"

retrieved_secret = client.get_secret("PythonClientSecret")

subscription_id = '7a9974b4-6ef3-490d-a02d-b9b3a07332f6'
credential = ClientSecretCredential(
    tenant_id='72f988bf-86f1-41af-91ab-2d7cd011db47',
    client_id='b381239e-4377-4a79-96fe-d7294581c552',
    client_secret= retrieved_secret.value
)

resource_group = os.getenv('resource_group')
WORKSPACE_NAME = os.getenv('WORKSPACE_NAME')
SKU = os.getenv('SKU')
Location = os.getenv('Location')
enable_no_public_ip = True if os.getenv('enable_no_public_ip') == 'True' else False
MRG = os.getenv('MRG')

base_url = 'https://management.azure.com'
polling_interval = 20
client = AzureDatabricksManagementClient(credential, subscription_id, base_url=base_url, polling_interval=20)

resource_group_params = {'location':'resource_group.Location'}

enable_no_public_ip = WorkspaceCustomBooleanParameter(value = enable_no_public_ip)

custom_parameters = WorkspaceCustomParameters(
    enable_no_public_ip = enable_no_public_ip,
)

workspace_params = {
    'location': Location,
    'managed_resource_group_id':str(MRG),
    'sku' : Sku(name = SKU),
    'tags': {'ReadWorkspace':'VSTerminal'}
    }

workspace_params.update(parameters=custom_parameters)

# #Get(read) a workspace
databricks_workspace = client.workspaces.get(resource_group, WORKSPACE_NAME)
print(databricks_workspace)