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
        data = self.dataframe.dtypes[self.dataframe.dtypes == np.object]
        columnNames = list(data.index)
        for i in columnNames:
            self.dataframe = self.dataframe.astype('category')
        return self.dataframe

    def normalizeData(self):
        scaler = preprocessing.MinMaxScaler()
        names = self.dataframe.columns
        d = scaler.fit_transform(self.dataframe)
        normalize_df = pd.DataFrame(d, columns = names)
        self.dataframe = normalize_df
        return self.dataframe
    
