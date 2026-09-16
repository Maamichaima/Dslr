from src.data.loader import DataLoader
from src.data.preprocessing import Preprocessing
from src.visualization.scatter import Scatter
from pathlib import Path

def main():
    current_file_dir = Path(__file__).resolve().parent
    loader = DataLoader(f"{current_file_dir}/../datasets/dataset_train.csv")
    df = loader.load()
    if df is None or df.empty:
        return

    prep = Preprocessing(df)
    scat = Scatter(prep)

    scat.plot('Astronomy', 'Defense Against the Dark Arts')

if __name__ == "__main__":
    main()