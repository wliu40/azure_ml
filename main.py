# install azure cli
# https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=powershell
import sys

# connect to azure before running the code.
# az login --tenant cb956b3e-0e1a-485c-a395-a000041d2695
# see your tenant_id from azureAD

import pandas as pd
import os
from azureml.core import Workspace
from azureml.core import Datastore, Dataset
from azureml.core import ScriptRunConfig
from azureml.core.experiment import Experiment
from azureml.core import Workspace, Dataset, Datastore


#import required libraries for workspace
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

#import required libraries for environments examples
from azure.ai.ml.entities import Environment, BuildContext

#Enter details of your AzureML workspace


subscription_id = 'efaef50b-3a01-4bf1-ad06-b63c101ab300'
resource_group = 'resource-group-1'
workspace_name = 'myworkspace'

workspace = Workspace(subscription_id, resource_group, workspace_name)
# workspace = Workspace.from_config("./config")
# workspace.write_config('./config')


# use later
env = workspace.environments['lightgbm']

# create it if not exist
new_experiment = Experiment(workspace=workspace, name="new_experiment_1")

# Create a script configuration
script_config = ScriptRunConfig(source_directory=os.getcwd(),
                                script="run_data_check.py",
                                environment=env,
                                compute_target='wliu08281')



# run code with customized command
# command = "bash bootstrap.sh && python train.py --learning_rate 1e-5".split()
#
# config = ScriptRunConfig(
#     source_directory='<path/to/code>',
#     command=command,
#     compute_target=compute_target,
#     environment=environment,
# )


# Submit a new run using the ScriptRunConfig, each submit will create a new run
# a *run* is a single trial of an experiment, in the run, you can log the metrics, save the outputs, and then you can
# use those metrics/artifacts to analyse this trial
new_run = new_experiment.submit(config=script_config)



# Create a wait for completion of the script
new_run.wait_for_completion()
















