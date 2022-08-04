from collections import namedtuple
from datetime import datetime
import uuid
from maintanance.config.configuration import configuration
from maintanance.logger import logging
from maintanance.exception import maintananceException
from maintanance.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from maintanance.entity.config_entity import DataIngestionconfig
from maintanance.component.data_ingestion import DataIngestion
from maintanance.component.data_validation import Datavalidation
import os,sys

class Pipeline:
    def __init__(self,config:configuration=configuration())->None:
        try:
            self.config=config

        except Exception as e:
            raise maintananceException(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion=DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()

        except Exception as e:
            raise maintananceException(e,sys) from e

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
            data_validation=Datavalidation(data_validation_config=self.config.get_data_validation_config(),
                                           data_ingestion_artifact=data_ingestion_artifact 
            )
            return data_validation.initiate_data_validation()
        except Exception as e:
            raise maintananceException(e,sys) from e

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass
    def run_pipeline(self):
        try:
            
            data_ingestion_artifact= self.start_data_ingestion()   
            self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            raise maintananceException(e,sys) from e