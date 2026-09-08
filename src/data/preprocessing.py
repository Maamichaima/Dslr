

"""
Data loading utilities for the DSLR project.
"""

import csv


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

    def load(self):
        """
        Load the CSV file.

        Returns:
            list[dict]: Dataset where each row is represented
            as a dictionary.

        Raises:
            FileNotFoundError: If the dataset does not exist.
            ValueError: If the CSV is empty.
        """
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                if reader.fieldnames is None:
                    raise ValueError("The CSV file is empty.")

                data = list(reader)

        except FileNotFoundError:
            raise FileNotFoundError(
                f"Dataset not found: {self.path}"
            )

        return data

    def columns(self):
        """
        Return the column names of the dataset.

        Returns:
            list[str]: CSV column names.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            return next(reader)

    def shape(self):
        """
        Return the number of rows and columns.

        Returns:
            tuple: (number_of_rows, number_of_columns)
        """
        data = self.load()

        return len(data), len(self.columns())