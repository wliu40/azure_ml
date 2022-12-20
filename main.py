import sys

from azureml.core import Workspace
from azureml.core import Environment
from azureml.core.runconfig import RunConfiguration

ws = Workspace.from_config()

## -----------------------------------------------------------------
print("Compute Resources:")
for compute_name in ws.compute_targets:
    compute = ws.compute_targets[compute_name]
    print("\t", compute.name, ':', compute.type)

## -----------------------------------------------------------------
print("Data Stores")
# Get the default datastore
default_ds = ws.get_default_datastore()
# Enumerate all datastores, indicating which is the default
for ds_name in ws.datastores:
    print(ds_name, "- Default =", ds_name == default_ds.name)


# # Create a Python environment for the experiment (from a .yml file)
experiment_env = Environment.from_conda_specification("experiment_env", "conda.yml")

# Register the environment
experiment_env.register(workspace=ws)
registered_env = Environment.get(ws, 'experiment_env')


sys.exit()