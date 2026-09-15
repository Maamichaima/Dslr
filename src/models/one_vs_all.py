import numpy as np

from src.models.logistic_regression import LogisticRegression


class OneVsAll:

    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations

        self.houses = [
            "Gryffindor",
            "Hufflepuff",
            "Ravenclaw",
            "Slytherin"
        ]

        self.models = {}
    def fit(self, X, house_column):
        """
		Train one logistic regression model for each house.
		"""

        for house in self.houses:

            # 1 = target house
            # 0 = all other houses
            y = []

            for student_house in house_column:
                if student_house == house:
                    y.append(1)
                else:
                    y.append(0)

            y = np.array(y)

            # Create a binary logistic regression model
            model = LogisticRegression(
                learning_rate=self.lr,
                iterations=self.iterations
            )

            # Train it
            model.fit(X, y)

            # Save the model
            self.models[house] = model

    def predict_proba(self, X):
        """
        Return probabilities for every house.
        """

        probabilities = {}

        for house in self.houses:

            model = self.models[house]

            probabilities[house] = model.predict(X)

        return probabilities
    def predict(self, X):
        """
        Predict the Hogwarts House.
        """

        probabilities = self.predict_proba(X)

        # Convert probabilities into a matrix
        scores = np.column_stack([
            probabilities[house]
            for house in self.houses
        ])

        # Get the index of the highest probability
        best_indices = np.argmax(scores, axis=1)

        # Convert indices to house names
        predictions = [
            self.houses[index]
            for index in best_indices
        ]

        return np.array(predictions)