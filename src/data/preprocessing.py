import pandas as pd


class Preprocessing:

	def __init__(self, df: pd.DataFrame):
		self.df = df
		self.numeric_cols = self.identify_numeric_columns(df)
		self.houses_column_name = "Hogwarts House"
		self.houses = df[self.houses_column_name].unique()

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
	
	def inspect_data(self, feature: str) -> dict:
		features = self.identify_numeric_columns()
 
		# print(f"{len(self.df)} étudiants chargés.")
		# print(f"{len(features)} features numériques trouvées :")
		# for f in features:
		# 	print(f"  - {f}")
	
		# print("\nExemple : répartition par maison pour 'Astronomy'")
		grouped = self.split_by_house(feature)#"Astronomy"

		return grouped
		# print (grouped)
		# for house, values in grouped.items():
		# 	print(f"  {house}: {len(values)} notes valides")
