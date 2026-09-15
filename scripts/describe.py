import sys
import math

from src.data.loader import DataLoader
from src.statistics.statistics import Statistics


def is_number(value):
    try:
        num = float(value)
        return not math.isnan(num)
    except (ValueError, TypeError):
        return False


def get_numeric_columns(df):

    numeric_columns = []

    for column in df.columns:

        values = df[column].dropna()

        if len(values) == 0:
            continue

        numeric_values = [
            value for value in values
            if is_number(value)
        ]

        if len(numeric_values) > 0:
            numeric_columns.append(column)

    return numeric_columns


def print_describe_table(df, numeric_columns):
    """
    Affiche les stats au format du sujet :
    features en colonnes, stats en lignes.
    """

    stats_order = ["Count", "Sum", "Mean", "Std", "Variance", "Min", "25%", "50%", "75%", "Max", "Range", "IQR"]

    # Calcul des stats pour chaque colonne numérique
    results = {}
    for column in numeric_columns:
        values = [float(v) for v in df[column] if is_number(v)]
        results[column] = Statistics.describe(values)

    # Largeur de chaque colonne
    col_widths = {}
    for column in numeric_columns:
        max_val_len = max(
            len(f"{results[column][stat]:.6f}") for stat in stats_order
        )
        col_widths[column] = max(len(column), max_val_len) + 2

    label_width = max(len(stat) for stat in stats_order) + 2

    # Ligne d'en-tête
    header = " " * label_width
    for column in numeric_columns:
        header += f"{column:>{col_widths[column]}}"
    print(header)

    # Une ligne par statistique
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
    loader.display(df.head())

    numeric_columns = get_numeric_columns(df)

    print_describe_table(df, numeric_columns)


if __name__ == "__main__":
    main()