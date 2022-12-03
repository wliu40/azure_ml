# install azure cli
# https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=powershell

# connect to azure before running the code.
# az login --tenant cb956b3e-0e1a-485c-a395-a000041d2695
# see your tenant_id from azureAD


from azureml.core import Workspace

#  Create a workspace
# ws = Workspace.create(name='myworkspace1',
#                       subscription_id='efaef50b-3a01-4bf1-ad06-b63c101ab300',
#                       resource_group='resource-group-1',
#                       create_resource_group=False,  # True if it does not exist
#                       location='East US 2')

# Write the config.json file to local directory
# ws.write_config(path="./config")


# use the existing workspace
ws0 = Workspace.get(name='myworkspace',
                      subscription_id='efaef50b-3a01-4bf1-ad06-b63c101ab300',
                      resource_group='resource-group-1',
                      location='East US 2')
ws0.get_details()

