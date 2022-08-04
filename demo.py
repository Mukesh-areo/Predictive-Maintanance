# to check the demo of the code
from maintanance.pipeline.pipeline import Pipeline
from maintanance.logger import logging
from maintanance.exception import maintananceException
import os,sys
from maintanance.config.configuration import configuration
def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
        #data_validation_config=configuration().get_data_validation_config()
        #print(data_validation_config)
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        raise maintananceException(e,sys) from e


if __name__=="__main__":
    main()