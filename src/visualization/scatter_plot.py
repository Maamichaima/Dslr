import matplotlib.pyplot as plt
import pandas as pd

class Scatter_plot:
	def __init__(self):
		pass
	# def scatter_plot_for_course(df: pd.DataFrame, feature: str):
	# 	plt.scatter(df)

	def scatter_plot___(data, feature1, feature2):

		x = []
		y = []

		for i in range(len(data)):
			value1 = data.iloc[i][feature1]
			value2 = data.iloc[i][feature2]

			if value1 == "" or value2 == "":
				continue

			x.append(float(value1))
			y.append(float(value2))

		plt.figure(figsize=(10, 6))

		plt.scatter(x, y)

		plt.xlabel(feature1)
		plt.ylabel(feature2)
		plt.title(f"{feature1} vs {feature2}")

		plt.show()

