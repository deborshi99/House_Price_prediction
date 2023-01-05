import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.utils import resample
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from utils.constants import DATA_TO_DROP
class dataPipeline:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
    
    def createPipeline(self):
        ### Remove the ID cols, reason please refer the datapreprocessing notebook #######
        for id_cols in DATA_TO_DROP:
            if id_cols in self.data.columns:
                self.data.drop(id_cols, axis=1, inplace=True)
                print(f"{id_cols} column has been dropped")
            else:
                print(f"{id_cols} column not found")
                pass
        
        return self.data

