from src.data.loader import DataLoader
from src.visualization.pair_plot import PairPlot
from pathlib import Path

def main():
    current_file_dir = Path(__file__).resolve().parent
    loader = DataLoader(f"{current_file_dir}/../datasets/dataset_train.csv")
    df = loader.load()
    if df is None or df.empty:
        return

    pplot = PairPlot(df)

    pplot.plot()

if __name__ == "__main__":
    main()