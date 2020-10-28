import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

#Return fitted model parameters to the dataset at datapath for each choice in degrees.
#Input: datapath as a string specifying a .txt file, degrees as a list of positive integers.
#Output: paramFits, a list with the same length as degrees, where paramFits[i] is the list of
#coefficients when fitting a polynomial of d = degrees[i].
def main(datapath, degrees):
    paramFits = []
    data = np.loadtxt(datapath)
    for degree in degrees:
        fm = feature_matrix(data[:,0], degree)
        paramFits.append(least_squares(fm, data[:,1]))
    return paramFits


#Return the feature matrix for fitting a polynomial of degree d based on the explanatory variable
#samples in x.
#Input: x as a list of the independent variable samples, and d as an integer.
#Output: X, a list of features for each sample, where X[i][j] corresponds to the jth coefficient
#for the ith sample. Viewed as a matrix, X should have dimension #samples by d+1.
def feature_matrix(x, d):
    X = [[xx ** dd for dd in range(d, -1, -1)] for xx in x]
    return X


#Return the least squares solution based on the feature matrix X and corresponding target variable samples in y.
#Input: X as a list of features for each sample, and y as a list of target variable samples.
#Output: B, a list of the fitted model parameters based on the least squares solution.
def least_squares(X, y):
    X = np.array(X)
    y = np.array(y)
    B = np.linalg.inv(X.T @ X) @ (X.T @ y)
    return B

if __name__ == '__main__':
    datapath = 'poly.txt'
    degrees = [1,2,3,4,5]

    paramFits = main(datapath, degrees)
    pprint(paramFits)
    x, y = np.loadtxt(datapath)[:,0], np.loadtxt(datapath)[:,1]
    plt.scatter(x,y,color='black')
    x.sort()
    for degree, paramFit in zip(degrees, paramFits):
        fm = np.array(feature_matrix(x, degree))
        Y = fm @ paramFit
        plt.plot(x, Y, label='Degree ' + str(degree))
    plt.legend()
    plt.show()

