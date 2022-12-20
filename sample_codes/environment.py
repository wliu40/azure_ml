# """ How to create a new environment, save and load an environment, and how to register it to your workspace, so that
#  you can use it later"""
#
# # https://azure.github.io/azureml-cheatsheets/docs/cheatsheets/python/v1/environment
#
# from azureml.core import Workspace, Dataset, Datastore
# from azureml.core.environment import Environment, CondaDependencies
#
#
# workspace = Workspace.from_config("D:/Azure_SDK/config")
#
# # list current environments
# for name, env in workspace.environments.items():
#     print(name, env)
#
# # get a specific version
# env = Environment.get(workspace, 'lightgbm', version=1)
#
# # create a new environment
# conda_dep = CondaDependencies()
# conda_dep.add_conda_package('python==3.8')
# conda_dep.add_conda_package('numpy==1.21.0')
# conda_dep.add_conda_package('pandas==1.4.0')
# conda_dep.get_default_number_of_packages()
# conda_dep.get_python_version()
# # save to yml file
# conda_dep.save('conda_env.yml')
#
#
# # load env from yml file
# # env = Environment.from_conda_specification('<env-name>', '<path/to/env.yml>')
#
#
# myenv = Environment(name='myenv')
# myenv.python.conda_dependencies = conda_dep
#
# # Register an environment env: Environment to your workspace ws to reuse/share with your team.
# myenv.register(workspace)
#
#
# # use later
# env = workspace.environments['myenv']
