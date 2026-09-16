from src.model.one_vs_all import OneVsAll
from src.data.preprocessing import Preprocessing
import sys
from src.data.loader import DataLoader

if __name__ == "__main__":
  if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)

  filepath = sys.argv[1]

  loader = DataLoader(filepath)
  df = loader.load()

  prep = Preprocessing(df)

  

  model = OneVsAll(prep, ["Divination", "History of Magic", "Charms", "Astronomy", "Transfiguration"])
  # model = OneVsAll(prep, ["Defense Against the Dark Arts", "Charms", "Divination", "Muggle Studies"])
  model.fit()
  model.save_all_weights()
