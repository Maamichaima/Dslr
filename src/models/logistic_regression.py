import numpy as np
import sys

class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = 0
        self.cost_history = []

    def sigmoid(self, z):
        """Sigmoid activation function"""
        z = np.clip(z, -500, 500)
        return 1 / (1 + np.exp(-z))


    def cost(self, y_pred, y):
        """Cross-entropy loss"""
        m = len(y)

        epsilon = 1e-15
        y_pred = np.clip(y_pred, epsilon, 1 - epsilon)

        return - (1 / m) * np.sum(
            y * np.log(y_pred) +
            (1 - y) * np.log(1 - y_pred)
        )

    def fit(self, X:np.array, y: np.array):
        """Train model using gradient descent"""
        m, n = X.shape
        self.weights = np.zeros(n)

        for _ in range(self.iterations):
            z = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(z)

            dw = (1/m) * np.dot(X.T, (y_pred - y))
            db = (1/m) * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            self.cost_history.append(self.cost(y_pred, y))

    def predict(self, X):
        """Make predictions"""
        return self.sigmoid(np.dot(X, self.weights))
