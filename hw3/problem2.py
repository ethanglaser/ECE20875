import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

f = 1
for dist in ['norm', 'cauchy', 'cosine', 'expon', 'uniform', 'laplace', 'wald', 'rayleigh']:
    for text in ['distA.csv', 'distB.csv', 'distC.csv']:
        plt.figure(f)
        f += 1
        stats.probplot(np.loadtxt(text), dist = dist, plot=plt)
        plt.savefig('Output/' + text.split('.')[0] + '_' + dist)