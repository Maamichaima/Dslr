from src.data.preprocessing import Preprocessing
from src.model.logistic_regression import LogisticRegression
import sys
from src.data.loader    import DataLoader
import json
import numpy as np


class LogregTrain:
  def __init__(self, prep: Preprocessing, features_name: list[str]):
    self.prep = prep
    self.features_name = features_name

  def fit(self):
    features = self.prep.prepare_features(self.features_name)
    labels = self.prep.get_labels(features)
    self.models = {}
    for house in self.prep.houses:
      model = LogisticRegression()
      model.fit(features.to_numpy(), self.prep.make_binary_labels(labels, house))
      self.models[house] = model
      

  def save_all_weights(self, file_name='weights.json'):
        data = {}
        for house, model in self.models.items():
            data[house] = {
                'weights': model.weights.tolist(),
                'bias': float(model.bias)
            }

        with open(file_name, 'w') as f:
            json.dump(data, f, indent=2)

  def load_all_weights(self, file_name='weights.json'):
        with open(file_name, 'r') as f:
            data = json.load(f)

        self.models = {}
        for house, values in data.items():
            model = LogisticRegression()
            model.weights = np.array(values['weights'])
            model.bias = values['bias']
            self.models[house] = model

if __name__ == "__main__":
  if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)

  filepath = sys.argv[1]

  loader = DataLoader(filepath)
  df = loader.load()

  prep = Preprocessing(df)

  model = LogregTrain(prep, ["Defense Against the Dark Arts", "Divination"])
  model.fit()
  model.save_all_weights()