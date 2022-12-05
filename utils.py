import os
from azureml.core import Workspace

def save_config_to_file(workspace, dst_dir='./config'):
    '''Write the config.json on your behalf. The path defaults to '.azureml/' in the current working directory
    and file_name defaults to 'config.json.'''
    if not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
    workspace.write_config(path=dst_dir)

def get_workspace_from_config_file(config_file_path='./config'):
    """Read the workspace configuration from config. The parameter defaults to
     starting the search in the current directory."""
    assert os.path.isfile(config_file_path)
    workspace = Workspace.from_config(config_file_path)
    return workspace

def upload_directory_to_datastore(datastore, local_src_dir, target_dir):
    datastore.upload(
        src_dir=local_src_dir,
        target_path=target_dir,
        overwrite=True,
    )

def upload_files_to_datastore(datastore, local_files, target_dir):
    datastore.upload_files(
        local_files,  # List[str] of absolute paths of files to upload
        target_path=target_dir,
        overwrite=False,
    )