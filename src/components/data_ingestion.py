import os 
import sys 
from src.exceptions import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts',"train.csv")
    test_data_path  = os.path.join('artifacts',"test.csv")
    raw_data_path  = os.path.join('artifacts',"data.csv")

#### this thing of upper code is the same as @dataClass , only use @dataclass if you have only attributes 
# class DataIngestionConfig:
#     def __init__(self):
#         self.train_data_path = os.path.join('artifacts',"train.csv")
#         self.test_data_path  = os.path.join('artifacts',"test.csv")
#         self.raw_data_path  = os.path.join('artifacts',"data.csv")

# config_path = DataIngestionConfig()
# print(config_path.train_data_path) 
# print(config_path.test_data_path)

class DataInjection:
    def __init__(self):
        self.injection_config = DataIngestionConfig()
    
    def initiate_data_injection(self):
        logging.info("Enter the data injection method or component ")
        try:
            file_path = r"C:\Users\wisen\MLproject\notebook\stud.csv"
            df = pd.read_csv(file_path)
            logging.info('Reading the dataset')

            os.makedirs(os.path.dirname(self.injection_config.train_data_path),exist_ok = True)

            df.to_csv(self.injection_config.raw_data_path, index= False , header= True)

            logging.info("Train test Split intiated")
            train_set ,test_set = train_test_split(df, test_size = 0.2 , random_state= 42)

            train_set.to_csv(self.injection_config.train_data_path, index = False , header = True)
            test_set.to_csv(self.injection_config.test_data_path, index = False , header = True)

            logging.info("Creating (injection) of Data (Training , Test and raw_data)")
             
            ### this Return is done so that i can use these some where else if need be 
            return (
                self.injection_config.train_data_path, 
                self.injection_config.test_data_path,
                self.injection_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == '__main__':
    obj = DataInjection()
    obj.initiate_data_injection()
 





        

