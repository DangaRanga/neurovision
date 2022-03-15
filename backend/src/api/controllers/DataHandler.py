from flask import flash
from sklearn import preprocessing
import numpy as np
import pandas as pd

class DataHandler():

    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def getDataFrame(self):
        return self.dataframe
    
    def removeFeature(self, featureName):
        self.dataframe.drop(featureName, inplace=True, axis=1)
    
    def translateData(self):
        # train.day = train.day.astype('category')
        mydataframe = self.dataframe
        data = mydataframe.dtypes[mydataframe.dtypes == np.object]
        columnNames = list(data.index)
        for i in columnNames:
            mydataframe[i] = mydataframe[i].astype('category')
            catagories = mydataframe[i].unique()
            for cat_index in range(len(catagories)):
                mydataframe[i] = mydataframe[i].replace([catagories[cat_index]], cat_index + 1)
        self.dataframe = mydataframe

    def normalizeData(self):
        scaler = preprocessing.MinMaxScaler()
        names = self.dataframe.columns
        d = scaler.fit_transform(self.dataframe)
        normalize_df = pd.DataFrame(d, columns = names)
        self.dataframe = normalize_df
    
