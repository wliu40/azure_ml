# install azure cli
# https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=powershell


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



workspace = Workspace.from_config("./config")

# create it if not exist
new_experiment = Experiment(workspace=workspace,
                            name="new_experiment_1")

# Create a script configuration
script_config = ScriptRunConfig(source_directory=".",
                                script="run_data_check.py")


# Submit a new run using the ScriptRunConfig
new_run = new_experiment.submit(config=script_config)


# Create a wait for completion of the script
new_run.wait_for_completion()













