import sys

from src.data.loader import DataLoader
from src.data.preprocessing import Preprocessing
from src.statistics.statistics import Statistics
from src.visualization.histogram import Histogram


def main():
	loader = DataLoader("/Users/maamichaima/Desktop/dslr/datasets/dataset_train.csv")
	df_train = loader.load()
      
	prep = Preprocessing(df_train)
	incepect_data = prep.split_by_house("Care of Magical Creatures")
	print(incepect_data["Gryffindor"])
      
	histogram = Histogram(df_train).histogram_for_course("Care of Magical Creatures", incepect_data)
    
	# plot_histogram(df_train, best_column)

if __name__ == "__main__":
    main()