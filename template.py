import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'Wine_quality'

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/comman.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        try:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file: {filename}")
        except Exception as e:
            logging.error(f"Error creating directory {filedir}: {e}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        try:
            with open(filepath, "w") as f:
                pass
            logging.info(f"Creating empty file: {filepath}")
        except Exception as e:
            logging.error(f"Error creating file {filepath}: {e}")
    else:
        logging.info(f"{filename} already exists")
