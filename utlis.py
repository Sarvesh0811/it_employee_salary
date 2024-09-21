import numpy as np
import pandas as pd
import pickle
import json
import config

class ITSalary():
    def __init__(self):
        pass  

    def __load_data(self):
        with open(config.MODEL_FILE_NAME, 'rb') as f:
            self.model = pickle.load(f)

        with open(config.COLUMN_DATA_JSON, 'r') as f:
            self.column_data = json.load(f)

        print("Column Data Loaded:", self.column_data)
        
        self.columns_name = self.model.feature_names_in_
        self.columns_count = self.model.n_features_in_

    def get_predicted_salary(self, Gender, Experience, Position):
        
        self.__load_data()
        Gender = self.column_data['Gender'][Gender]
        Position = "Position_" + Position
        Position_index = np.where(self.columns_name == Position)[0][0]

        test_array = pd.DataFrame(np.zeros((1, self.columns_count)), columns=self.columns_name)
        test_array.loc[0, self.columns_name[0]] = Gender
        test_array.loc[0, self.columns_name[1]] = Experience
        test_array.loc[0, Position] = 1

        predicted_salary = np.around(self.model.predict(test_array)[0], 3)
        print("Predicted Salary : ", predicted_salary)

        return predicted_salary

def load_dataset():
    df = pd.read_csv(config.CSV_FILE_NAME)
    return df

if __name__ == "__main__":
    salary = ITSalary()



