import sys
import matplotlib.pyplot as plt

from src.data.loader import DataLoader
from src.data.preprocessing import Preprocessing
from src.statistics.statistics import Statistics
from src.visualization.scatter_plot import Scatter_plot

def scatter_plot(data, feature1, feature2):

	houses = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}

	plt.figure(figsize=(10, 6))

	for house in houses:

		x = []
		y = []

		for i in range(len(data)):

			if data.iloc[i]["Hogwarts House"] != house:
				continue

			value_x = data.iloc[i][feature1]
			value_y = data.iloc[i][feature2]

			if value_x == "" or value_y == "":
				continue

			x.append(float(value_x))
			y.append(float(value_y))

		plt.scatter(
			x,
			y,
			color=houses[house],
			label=house,
			s=10
		)

	plt.xlabel(feature1)
	plt.ylabel(feature2)
	plt.title(f"{feature1} vs {feature2}")
	plt.legend()
	plt.show()

def main():
	loader = DataLoader("/Users/maamichaima/Desktop/dslr/datasets/dataset_train.csv")
	df_train = loader.load()
      
	prep = Preprocessing(df_train)
	Astronomy = prep.split_by_house("Astronomy")
	Herbology = prep.split_by_house("Defense Against the Dark Arts")
	print(df_train["Defense Against the Dark Arts"])
    
	scatter_plot(df_train,
		"Astronomy",
		"Defense Against the Dark Arts"
	)
      
	

if __name__ == "__main__":
    main()