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

        sorted_values = values.sort_values().reset_index(drop=True)

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
    def range(values):
        if len(values) == 0:
            return None

        return Statistics.maximum(values) - Statistics.minimum(values)

    @staticmethod
    def sum(values):
        if len(values) == 0:
            return None

        total = 0

        for value in values:
            total += value

        return total

    @staticmethod
    def iqr(values):
        if len(values) == 0:
            return None

        q1 = Statistics.percentile(values, 0.25)
        q3 = Statistics.percentile(values, 0.75)

        return q3 - q1

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
            "Max": Statistics.maximum(values),
            "Sum": Statistics.sum(values),
            "Range": Statistics.range(values),
            "IQR": Statistics.iqr(values)
        }