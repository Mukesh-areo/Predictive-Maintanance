# to check the demo of the code
from maintanance.pipeline.pipeline import Pipeline
from maintanance.logger import logging
from maintanance.exception import maintananceException
import os,sys
from maintanance.config.configuration import configuration
from maintanance.component.data_transformation import DataTransformation
def main():
    try:
        #pipeline=Pipeline()
        #pipeline.run_pipeline()

        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(configuration(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")
        #data_validation_config=configuration().get_data_transformation_config()
        #print(data_validation_config)
    #except Exception as e:
    #    logging.error(f"{e}")
   #     print(e)
  #      raise maintananceException(e,sys) from e


#if __name__=="__main__":
 #   main()

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()
