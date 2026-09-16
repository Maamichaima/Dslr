import csv
import pandas as pd
import sys

class DataLoader:

    def __init__(self, path):
        self.path = path

        self.df = None

    def load(self):

        # pd.set_option('display.max_columns', None)
        # pd.set_option('display.max_rows', None) 

        self.df = self._load_csv(self.path)

        if self.df is None or self.df.empty:
            sys.exit(1)

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
        print("-" * 80)

        print(data)

        print("-" * 80)
