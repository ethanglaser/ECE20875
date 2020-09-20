import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(hist):
    """
    takes a histogram of counts and creates a histogram of probabilities

    :param hist: list
    :return: list
    """
    final = []
    for entry in hist:
        final.append(entry/sum(hist))
    return final


def computeJ(histo, width):
    """
    takes histogram of counts, uses norm_histogram to convert to probabilties, it then calculates computeJ for one bin width

    :param histo: list 
    :param width: float
    :return: float
    """
    probs = norm_histogram(histo)
    print(2 / ((sum(histo) - 1) * width), (sum(histo) + 1) / ((sum(histo) - 1) * width), sum(p ** 2 for p in probs))
    J = 2 / ((sum(histo) - 1) * width) - (sum(histo) + 1) / ((sum(histo) - 1) * width) * sum(p ** 2 for p in probs)
    return J


def sweepN (data, minimum, maximum, min_bins, max_bins):
    """
    find the optimal bin
    calculate computeJ for a full sweep [min_bins to max_bins]
    please make sure max_bins is included in your sweep

    :param data: list
    :param minimum: int
    :param maximum: int
    :param min_bins: int
    :param max_bins: int
    :return: list
    """
    Js = []
    for bins in range(min_bins, max_bins + 1):
        newdata = [0] * bins
        for val in data:
            if val < maximum and val > minimum:
                newdata[int((val - minimum) / ((maximum - minimum) / bins))] += 1
        Js.append(computeJ(plt.hist(data, bins, (minimum, maximum))[0], (maximum - minimum) / bins))
    return Js


def findMin (l):
    """
    generic function that takes a list of numbers and returns smallest number in that list its index.
    return optimal value and the index of the optimal value as a tuple.

    :param l: list
    :return: tuple
    """
    return (min(l), l.index(min(l)))


if __name__ == '__main__':
    data = np.loadtxt('input.txt')  # reads data from input.txt
    lo = min(data)
    hi = max(data)
    bin_l=1
    bin_h=100
    print(norm_histogram(data))
    js = sweepN(data, lo, hi, bin_l,bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(findMin(js))
