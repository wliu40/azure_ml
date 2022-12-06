# install azure cli
# https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=powershell


# connect to azure before running the code.
# az login --tenant cb956b3e-0e1a-485c-a395-a000041d2695
# see your tenant_id from azureAD

import pandas as pd
import os
from azureml.core import Workspace
from azureml.core import Datastore, Dataset
from azureml.core.experiment import Experiment
from azureml.core import Workspace, Dataset, Datastore
from utils import get_workspace_from_config_file
from utils import upload_files_to_datastore, upload_directory_to_datastore

subscription_id = 'efaef50b-3a01-4bf1-ad06-b63c101ab300'
resource_group = 'resource-group-1'
workspace_name = 'myworkspace'
location = 'East US 2'

workspace = Workspace(subscription_id, resource_group, workspace_name)
datastore = Datastore.get(workspace, "data")  # or: datastore = workspace.datastores['data']
dataset = Dataset.Tabular.from_delimited_files(path=(datastore, 'Loan+Approval+Prediction.csv'))
df = dataset.to_pandas_dataframe()
df.head()


#  Create a workspace
# ws = Workspace.create(name='myworkspace1',
#                       subscription_id='efaef50b-3a01-4bf1-ad06-b63c101ab300',
#                       resource_group='resource-group-1',
#                       create_resource_group=False,  # True if it does not exist
#                       location='East US 2')

# Write the config.json file to local directory
# ws.write_config(path="./config")


experiment = Experiment(workspace=workspace, name='new_test_experiment')

# list the existing experiments
# list_experiments = Experiment.list(workspace)


# -----------------------------------------------------
# Run an experiment using start_logging method
# -----------------------------------------------------
new_run = experiment.start_logging(snapshot_directory=None)

# -----------------------------------------------------
# Do your stuff here

# Count the observations
total_observations = len(df)

# Get the null/missing values
nulldf = df.isnull().sum()

# -----------------------------------------------------
# Log metrics and Complete an experiment run
# -----------------------------------------------------
# Log the metrics to the workspace
new_run.log("Total Observations", total_observations)

# Log the missing data values
# this will put a metric under this run,
for columns in df.columns:
    new_run.log(columns, nulldf[columns])

new_run.complete()
















