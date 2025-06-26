import json
import pandas as pd

class DataLoader:
    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, 'r') as file:
            data = json.load(file)
        return data
