import pandas as pd


NON_FEATURE_COLUMNS = [
    "Index",
    "Hogwarts House",
    "First Name",
    "Last Name",
    "Birthday",
    "Best Hand",
]
 
HOUSES = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


class Preprocessing:

	def __init__(self, df: pd.DataFrame):
		self.df = df
		pass

	def get_feature_columns(self) -> list:
		"""Retourne la liste des colonnes numériques utilisables comme features
		(= toutes les colonnes sauf celles de NON_FEATURE_COLUMNS)."""
		return [col for col in self.df.columns if col not in NON_FEATURE_COLUMNS]

	def split_by_house(self, feature: str) -> dict:
		"""Pour une feature donnée, retourne un dict {maison: liste de notes}
		en retirant les valeurs manquantes (NaN) de CETTE feature uniquement.
	
		On isole le dropna par feature (et pas sur tout le dataframe) pour ne
		pas perdre inutilement des lignes valides sur d'autres colonnes.
		"""
		result = {}
		for house in HOUSES:
			subset = self.df[self.df["Hogwarts House"] == house][feature]
			values = subset.dropna().tolist()
			result[house] = values
		return result
	
	def get_feature_pair(self, feat_x: str, feat_y: str) -> pd.DataFrame:
		"""Retourne un sous-dataframe (Hogwarts House, feat_x, feat_y) en ne
		gardant que les lignes où LES DEUX features sont renseignées.
		Utile pour scatter_plot et pair_plot (on ne peut pas placer un point
		si l'une des deux coordonnées manque)."""
		cols = ["Hogwarts House", feat_x, feat_y]
		return self.df[cols].dropna()
	
	def inspect_data(self, feature: str) -> dict:
		features = self.get_feature_columns()
 
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
