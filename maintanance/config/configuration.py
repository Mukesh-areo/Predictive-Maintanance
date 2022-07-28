from maintanance.entity.config_entity import DataIngestionconfig,DataTransformationconfig,Datavalidationconfig,ModelTrainerconfig,ModelEvaluationconfig,ModelPusherconfig,Trainingpipelineconfig
class configuration:
    def __init__(self)-> None:
        pass

    def get_data_ingestion_config(self)->DataIngestionconfig:
        pass

    def get_data_validation_config(self)->Datavalidationconfig:
        pass

    def get_data_transformation_config(self)->DataTransformationconfig:
        pass

    def get_model_trainer_config(self)->ModelTrainerconfig:
        pass

    def get_model_evaluation_config(self)->ModelEvaluationconfig:
        pass

    def get_model_pusher_config(self)->ModelPusherconfig:
        pass

    def get_training_pipeline_config(self)->Trainingpipelineconfig:
        pass