import numpy as np
import sys
from src.data.loader    import DataLoader
from src.data.preprocessing import Preprocessing, FeatureScaler
import matplotlib.pyplot as plt

class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = 0
        self.cost_history = []

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def cost(self, y_pred, y):
        """Cross-entropy loss"""
        m = len(y)
        eps = 1e-15
        y_pred = np.clip(y_pred, eps, 1 - eps)
        return - (1/m) * np.sum(y*np.log(y_pred) + (1-y)*np.log(1-y_pred))

    def gradient_descent():
        pass

    def fit(self, X:np.array, y: np.array):
        m, n = X.shape
        self.weights = np.zeros(n)
        # indices = np.random.permutation(m)
        # X = X[indices]
        # y = y[indices]
        for _ in range(self.iterations):
            z = np.dot(X, self.weights) + self.bias
            y_pred = self.sigmoid(z)

            dw = (1/m) * np.dot(X.T, (y_pred - y))
            db = (1/m) * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

            self.cost_history.append(self.cost(y_pred, y))

    def fit_sgd(self, X:np.array, y: np.array):
        m, n = X.shape
        self.weights = np.zeros(n)
        self.bias = 0
        self.cost_history = []
        for _ in range(self.iterations):
            for i in range(m):
                xi = X[i]
                yi = y[i]

                zi = np.dot(xi, self.weights) + self.bias
                yi_pred = self.sigmoid(zi)

                dw = np.dot(xi.T, (yi_pred - yi))
                db = np.sum(yi_pred - yi)

                self.weights -= self.lr * dw
                self.bias -= self.lr * db

            z_full = np.dot(X, self.weights) + self.bias
            y_pred_full = self.sigmoid(z_full)
            self.cost_history.append(self.cost(y_pred_full, y))

    def fit_minibatch(self, X: np.array, y: np.array, batch_size=32):
        m, n = X.shape
        self.weights = np.zeros(n)
        self.bias = 0
        self.cost_history = []
        for _ in range(self.iterations):
            for start in range(0, m, batch_size):
                X_batch = X[start:start + batch_size]
                y_batch = y[start:start + batch_size]
                batch_m = X_batch.shape[0]

                z = np.dot(X_batch, self.weights) + self.bias
                y_pred = self.sigmoid(z)

                dw = (1/m) * np.dot(X_batch.T, (y_pred - y_batch))
                db = (1/m) * np.sum(y_pred - y_batch)

                self.weights -= self.lr * dw
                self.bias -= self.lr * db


            z_full = np.dot(X, self.weights) + self.bias
            y_pred_full = self.sigmoid(z_full)
            self.cost_history.append(self.cost(y_pred_full, y))  

    def predict(self, X):
        return self.sigmoid(np.dot(X, self.weights))
    
    def save_weitghs(self, file_name = 'weitghs.csv'):
        np.savetxt(file_name, np.append(self.weights, self.bias), delimiter=',')

    def load_weights(self, file_name = 'weitghs.csv'):
        arr = np.loadtxt(file_name, delimiter=',', dtype=float)
        self.weights = arr[:-1]
        self.bias = arr[-1]

    def plot_cost_history(self):
        plt.plot(self.cost_history)
        plt.xlabel('Epoch')
        plt.ylabel('Cost')
        plt.title('Training cost over epochs')
        plt.show()

if __name__ == "__main__":
  if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)

  filepath = sys.argv[1]

  loader = DataLoader(filepath)
  df = loader.load()

  prep = Preprocessing(df)
  scale = FeatureScaler()

  features_name = ["Defense Against the Dark Arts", "Divination"]

  features = prep.prepare_features(features_name)
  labels = prep.get_labels(features)
  # X_scaled = scale.fit_transform(features , features_name)
  # print(X_scaled)
#   print(features.to_numpy())
#   print(prep.make_binary_labels(labels, "Gryffindor"))
  model = LogisticRegression()

  model.fit(features.to_numpy(), prep.make_binary_labels(labels, "Gryffindor"))
  print(model.weights, model.bias)
  model.save_weitghs()
  model.load_weights()
  print(model.weights, model.bias)

#   print(model.predict([ -4.96394945 , 5.855]))

