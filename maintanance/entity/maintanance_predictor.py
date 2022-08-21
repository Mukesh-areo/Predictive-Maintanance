import os
import sys

from maintanance.exception import  maintananceException
from maintanance.utils.util import load_object

import pandas as pd


class MaintananceData:

    def __init__(self,
                 Cycle: int,
                 OpSet1: float,
                 OpSet2: float,
                 OpSet3: float,
                 SensorMeasure1: float,
                 SensorMeasure2: float,
                 SensorMeasure3: float,
                 SensorMeasure4: float,
                 SensorMeasure5: float,
                 SensorMeasure6: float,
                 SensorMeasure7: float,
                 SensorMeasure8: float,
                 SensorMeasure9: float,
                 SensorMeasure10: float,
                 SensorMeasure11: float,
                 SensorMeasure12: float,
                 SensorMeasure13: float,
                 SensorMeasure14: float,
                 SensorMeasure15: float,
                 SensorMeasure16: float,
                 SensorMeasure17: int,
                 SensorMeasure18: int,
                 SensorMeasure19: float,
                 SensorMeasure20: float,
                 SensorMeasure21: float,
                 Life_Ratio: float 
                 ):
        try:
            self.Cycle=Cycle
            self.OpSet1=OpSet1
            self.OpSet2=OpSet2
            self.OpSet3=OpSet3
            self.SensorMeasure1=SensorMeasure1
            self.SensorMeasure2=SensorMeasure2
            self.SensorMeasure3=SensorMeasure3
            self.SensorMeasure4=SensorMeasure4
            self.SensorMeasure5=SensorMeasure5
            self.SensorMeasure6=SensorMeasure6
            self.SensorMeasure7=SensorMeasure7
            self.SensorMeasure8=SensorMeasure8
            self.SensorMeasure9=SensorMeasure9
            self.SensorMeasure10=SensorMeasure10
            self.SensorMeasure11=SensorMeasure11
            self.SensorMeasure12=SensorMeasure12
            self.SensorMeasure13=SensorMeasure13
            self.SensorMeasure14=SensorMeasure14
            self.SensorMeasure15=SensorMeasure15
            self.SensorMeasure16=SensorMeasure16
            self.SensorMeasure17=SensorMeasure17
            self.SensorMeasure18=SensorMeasure18
            self.SensorMeasure19=SensorMeasure19
            self.SensorMeasure20=SensorMeasure20
            self.SensorMeasure21=SensorMeasure21
            self.Life_Ratio=Life_Ratio
           
        except Exception as e:
            raise maintananceException(e, sys) from e

    def get_maintanance_input_data_frame(self):

        try:
            maintanance_input_dict = self.get_maintanance_data_as_dict()
            return pd.DataFrame(maintanance_input_dict)
        except Exception as e:
            raise maintananceException(e, sys) from e

    def get_maintanance_data_as_dict(self):
        try:
            input_data = {
                "Cycle": [self.Cycle],
                "OpSet1": [self.OpSet1],
                "OpSet2": [self.OpSet2],
                "OpSet3": [self.OpSet3],
                "SensorMeasure1": [self.SensorMeasure1],
                "SensorMeasure2": [self.SensorMeasure2],
                "SensorMeasure3": [self.SensorMeasure3],
                "SensorMeasure4": [self.SensorMeasure4],
                "SensorMeasure5": [self.SensorMeasure5],
                "SensorMeasure6": [self.SensorMeasure6],
                "SensorMeasure7": [self.SensorMeasure7],
                "SensorMeasure8": [self.SensorMeasure8],
                "SensorMeasure9": [self.SensorMeasure9],
                "SensorMeasure10": [self.SensorMeasure10],
                "SensorMeasure11": [self.SensorMeasure11],
                "SensorMeasure12": [self.SensorMeasure12],
                "SensorMeasure13": [self.SensorMeasure13],
                "SensorMeasure14": [self.SensorMeasure14],
                "SensorMeasure15": [self.SensorMeasure15],
                "SensorMeasure16": [self.SensorMeasure16],
                "SensorMeasure17": [self.SensorMeasure17],
                "SensorMeasure18": [self.SensorMeasure18],
                "SensorMeasure19": [self.SensorMeasure19],
                "SensorMeasure20": [self.SensorMeasure20],
                "SensorMeasure21": [self.SensorMeasure21],
                "Life_Ratio": [self.Life_Ratio]}
            return input_data
        except Exception as e:
            raise maintananceException(e, sys)


class MaintanancePredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise maintananceException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise maintananceException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            maintanance_label_value = model.predict(X)
            if maintanance_label_value==0:
                return ("Engine was in good condition")
            elif maintanance_label_value==1:
                return ("Engine Performance was Reduced Need Maintanance")
            else :
                return ("Engine was in bad condition not safe to Fly")
        except Exception as e:
            raise maintananceException(e, sys) from e