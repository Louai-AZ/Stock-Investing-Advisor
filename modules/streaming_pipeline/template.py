import os
from pathlib import Path
import logging


list_of_files = [
    
    "deploy/Dockerfile"  ,
    "streaming_pipeline/__init__.py"  ,
    "tools/search.py"  ,
    
    ".env"  ,
    "Makefile"  ,
    "poetry.lock"  ,
    "pyproject.toml"  ,
    "logging.yaml"  ,
    ".dockerignore"

    ]


for filepath in list_of_files : 
    filepath = Path(filepath) 
    filedir , filename = os.path.split(filepath) 
    
    if filedir != "" : 
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0) :
        with open(filepath, 'w') as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")
    else :
        logging.info(f"{filename} is already exists")