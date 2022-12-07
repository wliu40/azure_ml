from azureml.core import Workspace

## -------------------- load workspace from config file------------------------------
# workspace = Workspace.from_config('./config')



## ----------------------------- save config to file -----------------------------
# Write the config.json file to local directory
# ws.write_config(path="./config")


## -------------------------- load workspace by args---------------------
# subscription_id = 'efaef50b-3a01-4bf1-ad06-b63c101ab300'
# resource_group = 'resource-group-1'
# workspace_name = 'myworkspace'
# location = 'East US 2'
# workspace = Workspace(subscription_id, resource_group, workspace_name)


## --------------------------- create a workspace ---------------------------------------
# ws = Workspace.create(name='myworkspace1',
#                       subscription_id='efaef50b-3a01-4bf1-ad06-b63c101ab300',
#                       resource_group='resource-group-1',
#                       create_resource_group=False,  # True if it does not exist
#                       location='East US 2')
