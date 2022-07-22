from distutils.command.install_data import install_data
from setuptools import setup
from typing import List

# Declaring variables for setup function
PROJECT_NAME = 'housing-predictor'
VERSION = '0.0.1'
AUTHOR = 'Chandan Kumar'
DESCRIPTION = "ML Project Deployment Process"
REQUIREMENT_FILE_NAME = 'requirements.txt'

def get_requirements_list()->List[str]:
    '''
    Function will return list of requirements mentioned in the requirements.txt
    '''
    with open(REQUIREMENT_FILE_NAME) as req_file:
        return req_file.readlines()


setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = ["housing"],
    install_requires = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())