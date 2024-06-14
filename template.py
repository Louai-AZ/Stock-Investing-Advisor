import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Stock-Investing-Advisor"


list_of_files = [
    ".github.com/workflows/.gitkeep",   # i'll use it whenever i'll be doing the cicd deployment (yaml file) / whenever i commit my code in github ,it'll automatically take the code to the cloud 
                                        # i create gitkeep file because when commiting to github , empty folder'll not be uploaded 
    
    ".github.com/workflows/cd_streaming_pipeline.yaml", 
    ".github.com/workflows/ci_financial_bot.yaml", 
    ".github.com/workflows/ci_streaming_pipeline.yaml", 
    ".github.com/workflows/ci_training_pipeline.yaml",       
    ".github.com/workflows/destroy_aws_infrastructure.yaml"                              









    # f"src/{project_name}/__init__.py",  # Constructur file
    # f"src/{project_name}/components/__init__.py", 
    # f"src/{project_name}/utils/__init__.py",
    # f"src/{project_name}/utils/common.py", # Inside this file, i'll write a ll my utility
    # f"src/{project_name}/logging/__init__.py",
    # f"src/{project_name}/config/__init__.py",
    # f"src/{project_name}/config/configuration.py",
    # f"src/{project_name}/pipeline/__init__.py",
    # f"src/{project_name}/entity/__init__.py",
    # f"src/{project_name}/constants/__init__.py",
    # "config/config.yaml",
    # "params.yaml", # Where i'm going to keep all my model parameters
    # "app.py",
    # "main.py",
    # "Dockerfile", # i'll build one docker image of our source code and do the deployment of that image to EC2
    # "requirements.txt",
    # "setup.py",
    # "notebooks/trials.ipynb",
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