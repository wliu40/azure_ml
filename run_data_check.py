
from azureml.core import Workspace, Datastore, Dataset, Experiment
from azureml.core import Run


# -------------------------- load a workspace -> get datastore -> get data -----------------
workspace = Workspace.from_config("./config")
datastore = Datastore.get(workspace, "data")  # or: datastore = workspace.datastores['data']
dataset = Dataset.Tabular.from_delimited_files(path=(datastore, 'Loan+Approval+Prediction.csv'))
df = dataset.to_pandas_dataframe()


sub_df = df[["Gender", "Married", "Education", "Loan_Status"]]
sub_df.to_csv("./outputs/loan_trunc.csv", index=False)

# print('The existing experiments: ')
# print(Experiment.list(workspace))

# load an experiment (if this experiment not exist, will create it)
experiment = Experiment(workspace=workspace, name='new_test_experiment')
new_run = Run.get_context()

# Log metrics and Complete an experiment run
new_run.log("df_size", len(df))
for col in df.columns:
    new_run.log(f"na_count_in_{col}", df[col].isnull().sum())

new_run.complete()



