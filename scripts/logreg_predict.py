from src.model.one_vs_all import OneVsAll
from src.data.preprocessing import Preprocessing
import sys
from src.data.loader import DataLoader

if __name__ == "__main__":
  if len(sys.argv) != 3:
        print("Usage: python describe.py <dataset.csv> <weights.json>")
        sys.exit(1)

  data_filepath = sys.argv[1]
  weights_filepath = sys.argv[2]

  print(data_filepath, weights_filepath)

  loader = DataLoader(data_filepath)
  df = loader.load()

  prep = Preprocessing(df)

  model = OneVsAll(prep, ["Defense Against the Dark Arts", "Divination"])
  model.load_all_weights(weights_filepath)

  features = prep.prepare_features(model.features_name)
  # print(features.loc[features.index, model.features_name])
  for index  in features.index:
      print(index, features.loc[index, model.features_name])