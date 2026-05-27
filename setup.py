'''
The setup.py file is used to specify the configuration for packaging and distributing a Python project. It typically includes information such as the project name, version, author, description, and dependencies. This file is essential for creating a distributable package that can be uploaded to PyPI or installed using pip.
'''

from setuptools import setup, find_packages
# find_packages is a utility function that automatically discovers all packages and subpackages in the project directory by recognizing the presence of __init__.py files. 
from typing import List

def get_requirements()->List[str]:
    """
    This function reads the requirements.txt file and returns a list of dependencies. 
    """

    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", 'r') as file:
            #  Read lines from the file
            lines = file.readlines()
            # Process each line 
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name = "ETL_pipeline",
    version = "0.0.1",
    author="Shreya",
    author_email="shreyakhandelwal7717@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)