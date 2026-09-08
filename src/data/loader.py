"""
Data loading utilities for the DSLR project.
"""

import csv
import pandas as pd


class DataLoader:
    """
    Load CSV datasets used by the project.

    This class is responsible only for reading the dataset.
    Data cleaning, statistics, visualization and preprocessing
    are handled by other components.
    """

    def __init__(self, train_path, test_path):
        """
        Initialize the data loader.

        Args:
            path (str): Path to the CSV dataset.
        """
        self.train_path = train_path
        self.test_path = test_path

        self.df_train = None
        self.df_test = None

    def load(self):
        self.df_train = self._load_csv(self.train_path)
        self.df_test = self._load_csv(self.test_path)

        return self.df_train, self.df_test

    def _load_csv(self, path):
        with open(path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        return pd.DataFrame(data)
    
    def display(self, data):
        """Display the first n rows of the dataset."""

        # for row in data[:n]:
        print("-" * 80)

        print(data)

        print("-" * 80)

    # def columns(self):
    #     """
    #     Return the column names of the dataset.

    #     Returns:
    #         list[str]: CSV column names.
    #     """
    #     with open(self.path, "r", encoding="utf-8") as file:
    #         reader = csv.reader(file)
    #         return next(reader)

    # def shape(self):
    #     """
    #     Return the number of rows and columns.

    #     Returns:
    #         tuple: (number_of_rows, number_of_columns)
    #     """
    #     data = self.load()

    #     return len(data), len(self.columns())