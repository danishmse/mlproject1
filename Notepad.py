##Code under setup.py

from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
    return requirements


setup(
name='mlproject1',
version='0.0.1',
author='danish',
author_email='iqbal.mse@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)

# Code under Template.py
import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)

project_name="mlproject"

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_transfer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirement.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
            with open(filepath, 'w') as f:
                 pass
                 logging.info("Creating empty file:{filepath}")
       
    else:
        logging.info(f"{filename} is already exist")
    
        

