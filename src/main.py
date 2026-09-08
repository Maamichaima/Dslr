from data.loader import DataLoader
from statistics.statistics import Statistics


def is_number(value):
    try:
        float(value)
        return True
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


def main():

    loader = DataLoader(
        "../datasets/dataset_train.csv",
        "../datasets/dataset_test.csv"
    )

    df_train, df_test = loader.load()

    print(df_train.describe())

    numeric_columns = get_numeric_columns(df_train)

    for column in numeric_columns:

        values = [
            float(value)
            for value in df_train[column]
            if is_number(value)
        ]

        result = Statistics.describe(values)

        print(column)
        print(result)
        print()


if __name__ == "__main__":
    main()