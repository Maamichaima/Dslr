import seaborn 
import matplotlib.pyplot as plt
from src.data.preprocessing import Preprocessing
import sys
from src.data.loader import DataLoader

class PairPlot:
  def __init__(self, df):
    self.df = df
    self.prep = Preprocessing(df)

  def plot(self):
      n = len(self.prep.numeric_cols)
      fig, axes = plt.subplots(n, n, figsize=(3*n, 3*n))

      houses = self.prep.houses
      for i, feat_y in enumerate(self.prep.numeric_cols):
          for j, feat_x in enumerate(self.prep.numeric_cols):
              ax = axes[i, j]

              if i == j:
                  data = self.prep.split_by_house(feat_x)
                  for house in houses:
                      ax.hist(data[house], alpha=0.5, label=house)
              else:
                  data = self.prep.get_feature_pair(feat_x, feat_y)
                  for house, (x, y) in data.items():
                    ax.scatter(x, y, label = house, alpha=0.4, s=8)

              ax.label_outer()

              if i == n - 1:
                  ax.set_xlabel(feat_x.replace(' ','\n'), fontsize=6)
              if j == 0:
                  ax.set_ylabel(feat_y.replace(' ','\n'), fontsize=6)

      # plt.tight_layout()
      handles, labels = axes[0, 1].get_legend_handles_labels()
      fig.legend(handles, labels, loc='upper right')
      plt.show()



if __name__ == "__main__":
  if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)

  filepath = sys.argv[1]

  loader = DataLoader(filepath)
  df = loader.load()

  pair = PairPlot(df)
  pair.plot()