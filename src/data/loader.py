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

    def __init__(self, path):
        """
        Initialize the data loader.

        Args:
            path (str): Path to the CSV dataset.
        """
        self.path = path

        self.df = None

    def load(self):

        # Display all columns
        pd.set_option('display.max_columns', None)
        # Display all rows
        pd.set_option('display.max_rows', None) 

        self.df = self._load_csv(self.path)

        return self.df

    def _load_csv(self, path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader)
                df = pd.DataFrame(reader, columns=header)
            return df
        except Exception as e:
            print(f"Something went wrong: {e}")

    def display(self, data):
        """Display the first n rows of the dataset."""

        # for row in data[:n]:
        print("-" * 80)

        print(data)

        print("-" * 80)
