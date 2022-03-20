import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


class ModelHandler(object):

    """
        Note the last value represents the output layer
        layers e.g [5,5,5]
        activation e.g [relu, relu, sigmoid]
    """

    def __init__(self, layers, activation) -> None:
        self.layers = layers
        self.activation = activation

    def createModel(self) -> None:
        options = []

        for i, num in enumerate(self.layers):
            options.append(Dense(num, self.activation[i]))

        self.model = Sequential(options)

        self.model.compile(
            optimizer="sgd", loss='binary_crossentropy', metrics=['accuracy'])

    def train(self, features, output, epochs, batch) -> None:
        return self.model.fit(features, output, epochs=epochs, batch_size=batch)

    def evaluate(self, features, output):
        return self.model.evaluate(features, output)

    def predict(self, features):
        return self.model.predict(features)
