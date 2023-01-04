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
        
        # numerical_data = [num for num in self.data.drop("hospital_death", axis=1).columns if self.data[num].dtype!="O"]
        # categorical_data = [cat for cat in self.data.drop("hospital_death", axis=1).columns if cat not in numerical_data]

        # #### getting highly correlated data #######################
        # corr = self.data.corr().abs()
        # upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(np.bool_))
        # to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
        # self.data.drop(to_drop, axis=1, inplace=True)

        # ### Updating the numerical and categorical column list
        # for not_req in to_drop:
        #     if not_req in numerical_data:
        #         numerical_data.remove(not_req)
        #     elif not_req in categorical_data:
        #         categorical_data.remove(not_req)
        #     else:
        #         pass
        
        ##### Oversampling the dataset #################

        data_majority = self.data[self.data.hospital_death == 0]
        data_minority = self.data[self.data.hospital_death == 1]
        if data_majority.shape[0] > data_minority.shape[0]:
            data_minority_upsampled = resample(
                data_minority,
                replace=True,
                n_samples=data_majority.shape[0],
                random_state=42
            )

            self.data = pd.concat([data_majority, data_minority_upsampled])
        elif data_minority.shape[0] > data_majority.shape[0]:
            data_majority_upsampled = resample(
                data_minority,
                replace=True,
                n_samples=data_minority.shape[0],
                random_state=42
            )

            self.data = pd.concat([data_majority, data_majority_upsampled])
        else:
            pass

        # features = self.data.drop('hospital_death', axis=1)
        # labels = self.data['hospital_death']
        # features = pd.get_dummies(features)
        # scaler = StandardScaler()
        # features = scaler.fit_transform(features)

        # X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

        return self.data#, features, labels, X_train, X_test, y_train, y_test

