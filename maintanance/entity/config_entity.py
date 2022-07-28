# creating the pipeline entity for all the stagge with namedtuple 
from collections import namedtuple

DataIngestionconfig=namedtuple('DataIngestionConfig',['dataset_download_url','tgz_download_dir','raw_data_dir','ingested_train_dir','ingested_test_dir'])

Datavalidationconfig=namedtuple('Datavalidationconfig',['schema_file_path'])

DataTransformationconfig= namedtuple('DataTransformationconfig',['transformed_train_dir','transformed_test_dir','preprocessed_object_file_path'])

ModelTrainerconfig=namedtuple('ModelTrainerconfig',['trained_model_file_path','base_accuracy'])

ModelEvaluationconfig=namedtuple('ModelEvaluationconfig',['model_evaluation_file_path','time_stamp'])

ModelPusherconfig=namedtuple=('ModelPusherconfig',['export_dir_path'])

Trainingpipelineconfig=namedtuple('Trainingpipelineconfig',['artifact_dir'])
