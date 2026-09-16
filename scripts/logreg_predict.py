from src.model.one_vs_all import OneVsAll
from src.data.preprocessing import Preprocessing
import sys
from src.data.loader import DataLoader
import csv

def predict_and_save(model: OneVsAll, output_file='houses.csv'):
    
    features = model.prep.prepare_features(model.features_name, prediction=True)

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Index', 'Hogwarts House'])

        for idx, row in features.iterrows():
            x = row.to_numpy()
            house, _ = model.predict(x)
            writer.writerow([idx, house])


if __name__ == "__main__":
  if len(sys.argv) != 3:
        print("Usage: python describe.py <dataset.csv> <weights.json>")
        sys.exit(1)

  data_filepath = sys.argv[1]
  weights_filepath = sys.argv[2]


  loader = DataLoader(data_filepath)
  df = loader.load()

  prep = Preprocessing(df)

  model = OneVsAll(prep, [])
  model.load_all_weights(weights_filepath)

  predict_and_save(model)