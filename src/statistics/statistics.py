import math

class Statistics:

    @staticmethod
    def count(values):
        return len(values)

    @staticmethod
    def mean(values):
        if len(values) == 0:
            return None

        total = 0

        for value in values:
            total += value

        return total / len(values)

    @staticmethod
    def minimum(values):
        if len(values) == 0:
            return None

        minimum = values[0]

        for value in values:
            if value < minimum:
                minimum = value

        return minimum

    @staticmethod
    def maximum(values):
        if len(values) == 0:
            return None

        maximum = values[0]

        for value in values:
            if value > maximum:
                maximum = value

        return maximum

    
    @staticmethod
    def standard_deviation(values):
        if len(values) == 0:
            return None

        mean = Statistics.mean(values)

        squared_sum = 0

        for value in values:
            squared_sum += (value - mean) ** 2

        variance = squared_sum / (len(values) - 1)

        return math.sqrt(variance)

    @staticmethod
    def percentile(values, percentage):
        if len(values) == 0:
            return None

        sorted_values = values.copy()
        sorted_values.sort()

        position = (len(sorted_values) - 1) * percentage

        lower = int(position)
        upper = lower + 1

        if upper >= len(sorted_values):
            return sorted_values[lower]

        fraction = position - lower

        return (
            sorted_values[lower]
            + fraction * (sorted_values[upper] - sorted_values[lower])
        )

    @staticmethod
    def describe(values):

        return {
            "Count": Statistics.count(values),
            "Mean": Statistics.mean(values),
            "Std": Statistics.standard_deviation(values),
            "Min": Statistics.minimum(values),
            "25%": Statistics.percentile(values, 0.25),
            "50%": Statistics.percentile(values, 0.50),
            "75%": Statistics.percentile(values, 0.75),
            "Max": Statistics.maximum(values)
        }

    # @staticmethod
    # def is_number(value):
    #     return True
    #     # except (ValueError, TypeError):
    #     #     return False

    # def get_numeric_columns(self, df):

    #     numeric_columns = []

    #     for column in df.columns:

    #         values = df[column].dropna()

    #         if len(values) == 0:
    #             continue

    #         if all(self.is_number(value) for value in values):
    #             numeric_columns.append(column)

    #     return numeric_columns