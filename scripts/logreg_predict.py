import sys

from src.data.loader import DataLoader
from src.data.preprocessing import Preprocessing
from src.models.logistic_regression import LogisticRegression
import numpy as np


def main():
    # Features:
    # [Math, History]
    X = np.array([
        [80, 70],
        [85, 75],
        [30, 40],
        [35, 45]
    ])

    # 1 = Gryffindor
    # 0 = Not Gryffindor
    y = np.array([1, 1, 0, 0])

    if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)

    filepath = sys.argv[1]

    loader = DataLoader(filepath)
    
    preprocessing = Preprocessing(loader.load())
    
    # 3. Choose the features
    features = [
        "Astronomy",
        "Herbology"
    ]

    # 4. Select features and remove rows with missing values
    X_df = preprocessing.prepare_features(features)

    # print(X_df)
    # 5. Get the corresponding houses
    house_column = preprocessing.df.loc[X_df.index, "Hogwarts House"]
    
    # print(house_column)

    # # 6. Create binary labels
    # Gryffindor = 1
    # Other houses = 0
    y = preprocessing.make_binary_labels(
        house_column,
        "Gryffindor"
    )
    
    # print(y)

    # # 7. Convert DataFrame to NumPy array
    X = X_df.to_numpy()
    


    # # Create model
    model = LogisticRegression(
        learning_rate=0.01,
        iterations=1000
    )

    # # Train
    model.fit(X, y)

    # # Probabilities
    probabilities = model.sigmoid(
        np.dot(X, model.weights) + model.bias
    )

    # # Predictions
    predictions = model.predict(X)

    # print("Weights:")
    # print(model.weights)

    # print("\nBias:")
    # print(model.bias)

    # print("\nProbabilities:")
    # print(probabilities)

    # print("\nPredictions:")
    # print(predictions)

    # print("\nReal values:")
    # print(y)


if __name__ == "__main__":
    main()