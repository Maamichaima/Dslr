import sys

from src.data.loader import DataLoader
from src.data.preprocessing import Preprocessing
from src.models.logistic_regression import LogisticRegression
import numpy as np

from src.models.one_vs_all import OneVsAll


def main():

    # Load dataset
    if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)

    filepath = sys.argv[1]

    loader = DataLoader(filepath)
    df = loader.load()

    # Preprocessing
    preprocessing = Preprocessing(df)

    features = [
        "Astronomy",
        "Herbology"
    ]

    # Select features and remove missing rows
    X_df = preprocessing.prepare_features(features)

    # Keep the corresponding houses
    house_column = df.loc[X_df.index, "Hogwarts House"]

    # Convert X to NumPy
    X = np.array(X_df, dtype=float)

    print("\nX shape:")
    print(X.shape)

    print("\nHouses:")
    print(house_column.head())

    # One-vs-All
    model = OneVsAll(
        learning_rate=0.01,
        iterations=1000
    )

    # Train 4 models
    model.fit(X, house_column.to_numpy())

    # Predict
    predictions = model.predict(X)

    print("\nPredictions:")
    print(predictions[:20])

    print("\nReal houses:")
    print(house_column.to_numpy()[:20])

    # Accuracy
    accuracy = np.mean(
        predictions == house_column.to_numpy()
    )



if __name__ == "__main__":
    main()