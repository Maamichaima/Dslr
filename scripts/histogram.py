
from src.data.loader import DataLoader
from src.statistics.statistics import Statistics
from src.visualization.histogram import (
    get_numeric_columns,
    find_most_homogeneous_course,
    plot_histogram,
)

def main():
	loader = DataLoader("../datasets/dataset_train.csv")
	df_train = loader.load()
	numeric_columns = get_numeric_columns(df_train)
      
	plot_histogram(df_train, best_column)

if __name__ == "__main__":
    main()