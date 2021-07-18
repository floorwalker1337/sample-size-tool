import numpy as np
import csv

class Model:
    def __init__(self, filepath):
        self.data = self.OpenData(filepath)

    def OpenData(self, filepath):
        if filepath[-4:-1] != '.csv':
            print("Please select a CSV file.")
            return -1
        with open (filepath, newline='') as csvfile: 
            pass


class QTable:
    def __init__(self):
        pass