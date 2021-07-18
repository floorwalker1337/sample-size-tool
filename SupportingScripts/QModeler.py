import tensorflow as tf
import numpy as np
from tensorflow import keras
import csv

# Get data from CSV files
csvNames = ["alpha_equals_0.csv"]
for name in csvNames:
    xValues = []
    lowerBounds = []
    upperBounds = []
    with open(name, newline='') as csvFile:
        dataReader = csv.reader(csvFile, delimiter=',')
        i = 0
        for row in dataReader:
            if (i!=0):
                xValues.append(int(row[0]))
                lowerBounds.append(float(row[1]))
                upperBounds.append(float(row[2]))
            i += 1

xValues = np.array(xValues, dtype=float)
lowerBounds = np.array(lowerBounds, dtype=float)
upperBounds = np.array(upperBounds, dtype=float)

# Define network
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

# Provide data to model
model.fit(xValues, upperBounds, epochs=500)
