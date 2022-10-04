import os
from pathlib import Path # This will help our application os independent, as finds out the type of operating system we are in and appends the path in that way
import logging

logging.basicConfig(
    level= logging.INFO, 
    format= "[%(asctime)s: %(levelname)s]: %(message)s"
    ) # The logs will be printed in the terminal in this format

while True:
    project_name = input("Enter the project name: ")
    if project_name!="":
        break

logging.info(f"Creating project by name: {project_name}")

# list of files:
list_of_files = [
    ".github/workflows/.gitkeep", # We want to create this folder structure for our github actions, and gitkeep is just a dummy file to upload the folder structure in github as github doesn't allow us to upload empty folders
    f"src/{project_name}/__init__.py" # The main project folder where all the required code is present
    f"tests/__init__.py", # 
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py", 
    "init_setup.sh", # For basic enviroment setup like python venv or conda env
    "requirements.txt", # required packages for our project
    "requirements_dev.txt", # only the packages required for testing our project like pytest
    "setup.py", # This will help us to do the basic setup; we need some more files for this setup (refer: https://packaging.python.org/en/latest/tutorials/packaging-projects/#a-simple-project)
    "pyproject.toml", # As per the packaging project link above, we need this for our project setup
    "setup.cfg", # 
    "tox.ini" # This will help us to test our python application in various environments
]

# Creating the above list of files

for filepath in list_of_files:
    filepath = Path(filepath) # this will convert the format of the file path we have in the above list as per the OS it is running in
    filedir, filename = os.path.split(filepath) # This will separate directory and file as a tuple (os.path.split("foldername/filename.txt") -> "foldername/", "filename.txt")
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # If the directory of file you want to create exists already, just leave it and don't throw any error.
        logging.info(f"Creating a directory at: {filedir} for file: {filename}")
    # If we create a file that is already present with some data in it, we will create it again and lose the existing data in the file.
    # So, we have to create the file only if it is not already present and has some data in it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            # pass # We are just creating the file and not writing anything
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")
    