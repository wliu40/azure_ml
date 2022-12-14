# https://learn.microsoft.com/en-us/azure/machine-learning/v1/how-to-track-monitor-analyze-runs?tabs=python
# https://learn.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py&preserve-view=true
from azureml.core import Workspace, Datastore, Dataset, Experiment


ws                = Workspace.from_config("../config")
az_store          = Datastore.get(ws, 'data')  # from ws get 'data' datastore
az_dataset        = Dataset.Tabular.from_delimited_files(path=(az_store, 'Loan+Approval+Prediction.csv'))
df = az_dataset.to_pandas_dataframe()


# -----------------------------------------------------
# Run an experiment using start_logging method
# -----------------------------------------------------
experiment = Experiment(workspace=ws, name="new_experiment_1")
new_run = experiment.start_logging(snapshot_directory=None)

# -----------------------------------------------------
# Log metrics and Complete an experiment run
# -----------------------------------------------------

# Log the metrics to the workspace
new_run.log("Total Observations", len(df))

# Log metrics and Complete an experiment run
new_run.log("df_size", len(df))
for col in df.columns:
    new_run.log(f"na_count_in_{col}", df[col].isnull().sum())

new_run.complete()
exit()


