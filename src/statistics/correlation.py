from itertools import combinations
from .statistics import Statistics

def find_most_correlated_pair(df, numeric_cols):
    best_pair = None
    best_r = 0

    for col1, col2 in combinations(numeric_cols, 2):
        pair_df = df[[col1, col2]].replace('', None).astype(float).dropna()
        # x = pair_df[col1].astype(float)
        # y = pair_df[col2].astype(float)

        r = pearson_correlation(pair_df[col1], pair_df[col2])

        if abs(r) > abs(best_r):
            best_r = r
            best_pair = (col1, col2)

    return best_pair, best_r


def pearson_correlation(x, y):
    n = len(x)
    mean_x = Statistics.mean(x)
    mean_y = Statistics.mean(y)
    std_x = Statistics.standard_deviation(x)
    std_y = Statistics.standard_deviation(y)

    covariance_sum = 0

    for x_i, y_i in zip(x, y):
        covariance_sum += (x_i - mean_x) * (y_i - mean_y)

    r = covariance_sum / ((n - 1) * std_x * std_y)
    return r