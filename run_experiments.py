# How to start an experiment
# how to log the artifacts to cloud

import os
import json
import azureml.core
from azureml.core import Workspace
from azureml.core import Experiment
import pandas as pd
import matplotlib.pyplot as plt

# Load the workspace from the saved config file
ws = Workspace.from_config()
print('Ready to use Azure ML {} to work with {}'.format(azureml.core.VERSION, ws.name))

# Create an Azure ML experiment in your workspace
experiment = Experiment(workspace=ws, name="mslearn-diabetes")

# Start logging data from the experiment, obtaining a reference to the experiment run
run = experiment.start_logging(snapshot_directory=None)

# if you donot pass snapshot_directory=None, you will get an error message:
# "message": "Failed to take a snapshot of .. Pass snapshot_directory=None
# # to start_logging to skip taking a snapshot of the given directory."

print("Starting experiment:", experiment.name)

# load the data from a local file
data = pd.read_csv('data/diabetes.csv')

# Count the rows and log the result
row_count = (len(data))
run.log('observations', row_count)
print('Analyzing {} rows of data'.format(row_count))

# Plot and log the count of diabetic vs non-diabetic patients
diabetic_counts = data['Diabetic'].value_counts()
fig = plt.figure(figsize=(6, 6))
ax = fig.gca()
diabetic_counts.plot.bar(ax=ax)
ax.set_title('Patients with Diabetes')
ax.set_xlabel('Diagnosis')
ax.set_ylabel('Patients')
plt.show()
run.log_image(name='label distribution', plot=fig)

# log distinct pregnancy counts
pregnancies = data.Pregnancies.unique()
run.log_list('pregnancy categories', pregnancies)

# Log summary statistics for numeric columns
med_columns = ['PlasmaGlucose', 'DiastolicBloodPressure', 'TricepsThickness', 'SerumInsulin', 'BMI']
summary_stats = data[med_columns].describe().to_dict()
for col in summary_stats:
    keys = list(summary_stats[col].keys())
    values = list(summary_stats[col].values())
    for index in range(len(keys)):
        run.log_row(col, stat=keys[index], value=values[index])

# Save a sample of the data and upload it to the experiment output
data.sample(100).to_csv('sample.csv', index=False, header=True)
run.upload_file(name='outputs/sample.csv', path_or_stream='./sample.csv')

# Complete the run
run.complete()


# Get logged metrics
print("Metrics:")
metrics = run.get_metrics()
for metric_name in metrics:
    print(metric_name, ":", metrics[metric_name])

# Get output files
print("\nFiles:")
files = run.get_file_names()
for file in files:
    print(file)


# download the artifacts

download_folder = 'downloaded-files'

# Download files in the "outputs" folder
run.download_files(prefix='outputs', output_directory=download_folder)

# Verify the files have been downloaded
for root, directories, filenames in os.walk(download_folder):
    for filename in filenames:
        print(os.path.join(root, filename))

run.get_details_with_logs()

# this is all the details for this run
#{'runId': 'b8ba110f-ba95-4f48-a901-f66a6ae43dd6',
# 'target': 'local',
# 'status': 'Completed',
# 'startTimeUtc': '2022-12-20T15:58:28.567196Z',
# 'endTimeUtc': '2022-12-20T16:00:50.535626Z', 'services': {},
# 'properties': {'azureml.git.repository_uri': 'https://github.com/wliu40/azure_ml.git',
# 'mlflow.source.git.repoURL': 'https://github.com/wliu40/azure_ml.git',
# 'azureml.git.branch': 'main',
# 'mlflow.source.git.branch': 'main',
# 'azureml.git.commit': 'c6e253b42d5a89d122b5cca70398ad02c9b37349',
# 'mlflow.source.git.commit': 'c6e253b42d5a89d122b5cca70398ad02c9b37349',
# 'azureml.git.dirty': 'True'}, 'inputDatasets': [], 'outputDatasets': [], 'logFiles': {}, 'submittedBy': 'Wei Liu'}
