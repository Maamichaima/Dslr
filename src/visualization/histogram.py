import matplotlib.pyplot as plt
from src.data.preprocessing import Preprocessing
import sys
from src.data.loader    import DataLoader

class Histogram:
  def __init__(self, prep):
    self.prep = prep

  def plot(self, feature: str):
    data = self.prep.split_by_house(feature)
    houses = self.prep.houses
    for house in houses:
      plt.hist(data[house], alpha=0.5, label=house)

    plt.legend()
    plt.xlabel('Marks')
    plt.ylabel('Number of student')
    plt.title(feature)
    plt.show()

  def plots(self):
    features = self.prep.numeric_cols
    for feature in features:
      self.plot(feature)

    

if __name__ == "__main__":
  if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)

  filepath = sys.argv[1]

  loader = DataLoader(filepath)
  df = loader.load()

  prep = Preprocessing(df)


  hist = Histogram(prep)
  # hist.plots()
  hist.plot("Care of Magical Creatures")

