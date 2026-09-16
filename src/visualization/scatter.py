from src.data.preprocessing import Preprocessing
import matplotlib.pyplot as plt
import sys
from src.data.loader import DataLoader
from itertools import combinations


class Scatter:
  def __init__(self, prep: Preprocessing):
    self.prep = prep

  def plot(self, feat_x: str, feat_y: str):
    data = self.prep.get_feature_pair(feat_x, feat_y)

    for house, (x, y) in data.items():
      plt.scatter(x, y, alpha=0.5, label=house)

    plt.legend()
    plt.xlabel(feat_x)
    plt.ylabel(feat_y)
    plt.show()

  def plots(self):
    for col1, col2 in combinations(self.prep.numeric_cols, 2):
        self.plot(col1, col2)


if __name__ == "__main__":
  if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)

  filepath = sys.argv[1]

  loader = DataLoader(filepath)
  df = loader.load()
  prep = Preprocessing(df)


  scat = Scatter(prep)
  # scat.plots()
  scat.plot('Astronomy', 'Defense Against the Dark Arts')
