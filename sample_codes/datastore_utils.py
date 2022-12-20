from azureml.core import Workspace, Datastore, Dataset, Experiment

## --------------- get datascore in workspace----------------------------
# datastore = Datastore.get(workspace, "data")  # or: datastore = workspace.datastores['data']

## --------------- upload a directory to datastore----------------------------
# datastore.upload(
#     src_dir=local_src_dir,
#     target_path=target_dir,
#     overwrite=True,
# )

## --------------- upload files to datastore----------------------------
# datastore.upload_files(
#     local_files,  # List[str] of absolute paths of files to upload
#     target_path=target_dir,
#     overwrite=False,
# )

## ---------------------------------load data from datastore -----------------------------------
# workspace = Workspace.from_config("./config")
# datastore = Datastore.get(workspace, "data")  # or: datastore = workspace.datastores['data']
# dataset = Dataset.Tabular.from_delimited_files(path=(datastore, 'Loan+Approval+Prediction.csv'))
# df = dataset.to_pandas_dataframe()