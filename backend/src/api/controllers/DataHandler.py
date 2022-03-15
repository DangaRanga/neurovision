from flask import flash
from sklearn import preprocessing
import numpy as np
import pandas as pd

class DataHandler():

    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def getDataFrame():
        return self.dataframe
    
    def removeFeature(featureName):
        self.dataframe.drop(featureName, inplace=True, axis=1)
    
    def normalizeData():
        scaler = preprocessing.MinMaxScaler()
        names = self.dataframe.columns
        d = scaler.fit_transform(self.dataframe)
        normalize_df = pd.DataFrame(d, columns = names)
        self.dataframe = normalize_df
        return self.dataframe
    
