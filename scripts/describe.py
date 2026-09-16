import sys

from src.data.loader import DataLoader
from src.statistics.statistics import Statistics


def print_describe_table(df):

    stats_order = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max", "Range", "IQR", "Sum"]

    numeric_columns = []
    results = {}
    for col_name in df.columns:
        try:
            col_values = df[col_name].replace('', None).dropna().astype(float)
            numeric_columns.append(col_name)
            results[col_name] = Statistics.describe(col_values)
        except ValueError:
            continue

    col_widths = {}
    for column in numeric_columns:
        max_val_len = max(
            len(f"{results[column][stat]:.6f}") for stat in stats_order
        )
        col_widths[column] = max(len(column), max_val_len) + 2

    label_width = max(len(stat) for stat in stats_order) + 2

    header = " " * label_width
    for column in numeric_columns:
        header += f"{column:>{col_widths[column]}}"
    print(header)

    for stat in stats_order:
        line = f"{stat:<{label_width}}"
        for column in numeric_columns:
            value = results[column][stat]
            line += f"{value:>{col_widths[column]}.6f}"
        print(line)


def main():

    if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)

    filepath = sys.argv[1]

    loader = DataLoader(filepath)
    df = loader.load()

    print_describe_table(df)


if __name__ == "__main__":
    main()