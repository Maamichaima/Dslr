import math


class Statistics:

    @staticmethod
    def count(values):
        """Return the number of values in the dataset."""
        return len(values)

    @staticmethod
    def mean(values):
        """Calculate and return the arithmetic mean of the values."""
        if len(values) == 0:
            return None

        total = 0

        for value in values:
            total += value

        return total / len(values)

    @staticmethod
    def minimum(values):
        """Find and return the smallest value in the dataset."""
        if len(values) == 0:
            return None

        minimum = values[0]

        for value in values:
            if value < minimum:
                minimum = value

        return minimum

    @staticmethod
    def maximum(values):
        """Find and return the largest value in the dataset."""
        if len(values) == 0:
            return None

        maximum = values[0]

        for value in values:
            if value > maximum:
                maximum = value

        return maximum

    @staticmethod
    def standard_deviation(values):
        """
        Calculate the sample standard deviation.

        Standard deviation measures how spread out the values
        are around the mean. It is the square root of variance.
        """
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
        """
        Calculate a percentile using linear interpolation.

        The percentile indicates the value below which a
        given percentage of the data falls.
        """
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
    def variance(values):
        """Calculate the sample variance as the square of the standard deviation."""
        if len(values) < 2:
            return None
            
        std = Statistics.standard_deviation(values)

        return std ** 2

    @staticmethod
    def range(values):
        """
        Calculate the range of the dataset.

        Range is the difference between the maximum
        and minimum values.
        """
        if len(values) == 0:
            return None

        return Statistics.maximum(values) - Statistics.minimum(values)

    @staticmethod
    def sum(values):
        """Calculate and return the sum of all values."""
        if len(values) == 0:
            return None

        total = 0

        for value in values:
            total += value

        return total

    @staticmethod
    def iqr(values):
        """
        Calculate the Interquartile Range (IQR).

        IQR measures the spread of the middle 50% of
        the data and is calculated as Q3 minus Q1.
        """
        if len(values) == 0:
            return None

        q1 = Statistics.percentile(values, 0.25)
        q3 = Statistics.percentile(values, 0.75)

        return q3 - q1

    @staticmethod
    def describe(values):
        """
        Calculate and return the main descriptive statistics
        for a dataset.
        """
        return {
            "Count": Statistics.count(values),
            "Sum": Statistics.sum(values),
            "Mean": Statistics.mean(values),
            "Std": Statistics.standard_deviation(values),
            "Variance": Statistics.variance(values),
            "Min": Statistics.minimum(values),
            "25%": Statistics.percentile(values, 0.25),
            "50%": Statistics.percentile(values, 0.50),
            "75%": Statistics.percentile(values, 0.75),
            "Max": Statistics.maximum(values),
            "Range": Statistics.range(values),
            "IQR": Statistics.iqr(values)
        }