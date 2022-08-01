import yaml
import sys,os 
from maintanance.exception import maintananceException
def read_yaml_file(file_path:str)->dict:
    """To read a YAML file and returns the contents as a dictonary
        file path:str
    """
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise maintananceException(e,sys) from e
