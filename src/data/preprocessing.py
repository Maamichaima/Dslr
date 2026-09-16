import pandas as pd
import numpy as np
from src.statistics.statistics import Statistics
import sys

class Preprocessing:

	def __init__(self, df: pd.DataFrame):
		self.df = df
		self.numeric_cols = self.identify_numeric_columns(df)
		if len(self.numeric_cols) == 0:
			print("No numeric colums found")
			sys.exit(1)

		self.houses_column_name = "Hogwarts House"
		if self.houses_column_name not in df.columns:
			print(f"Column '{self.houses_column_name}' not found in dataset")
			sys.exit(1)

		self.houses = df[self.houses_column_name].unique()

		self.feature_scaler = FeatureScaler()

	def identify_numeric_columns(self, df):
			numeric_cols = []
			for col in df.columns:
					try:
							df[col].replace('', None).dropna().astype(float)
							numeric_cols.append(col)
					except ValueError:
							continue
			return numeric_cols

	def split_by_house(self, feature: str) -> dict:
		result = {}
		for house in self.houses:
			subset = self.df[self.df[self.houses_column_name] == house][feature]
			values = subset.replace('', None).dropna().astype(float).tolist()
			result[house] = values
		return result
	
	def get_feature_pair(self, feat_x: str, feat_y: str) -> pd.DataFrame:
		result = {}
		for house in self.houses:
			subset = self.df[self.df['Hogwarts House'] == house]
			pair = subset[[feat_x, feat_y]].replace('', None).astype(float).dropna()
			result[house] = (pair[feat_x], pair[feat_y])
		return result

	def make_binary_labels(self, house_column, target_house):
		labels = []
		for house in house_column:
			if house == target_house:
				labels.append(1)
			else:
				labels.append(0)
		
		return np.array(labels)

	def prepare_features(self, desired_features_name: list[str], prediction = False):
		data = self.df[desired_features_name].replace('', None).astype(float)
		# print(data)
		if not prediction:
			self.feature_scaler.fit(data.dropna(), desired_features_name)
		# print(self.feature_scaler.means)
		data = data.fillna(self.feature_scaler.means)
		# print(data)
		return self.feature_scaler.transform(data, desired_features_name)

	def get_labels(self, features: pd.DataFrame) -> pd.DataFrame:
		return self.df.loc[features.index, "Hogwarts House"]


class FeatureScaler:
    def __init__(self):
        self.means = {}
        self.stds = {}

    def fit(self, X, feature_names):

        for col in feature_names:
            mean = Statistics.mean(X[col])
            std = Statistics.standard_deviation(X[col])

            self.means[col] = mean
            self.stds[col] = std

    def transform(self, X, feature_names):
        X_scaled = X.copy()
        for col in feature_names:
            X_scaled[col] = (X[col] - self.means[col]) / self.stds[col]
        return X_scaled