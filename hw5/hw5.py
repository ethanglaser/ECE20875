import numpy as np
from scipy import stats

#1.1
#H0: mu = 0.75
#H1: mu != 0.75
#z-test - large sample size

#1.2
def getVals(filename):
    myFile = open(filename)
    data = myFile.readlines()
    myFile.close()
    data = [float(x) for x in data]
    avg = np.mean(data)
    sd = np.std(data, ddof=1)
    n = len(data)
    se = sd / n ** 0.5
    z_c = (avg - 0.75) / se
    p = 2* stats.norm.cdf(z_c)
    return avg, sd, se, p, z_c


avg, sd, se, p, z_c = getVals('eng1.txt')
#p = t.cdf(t_c, df)
#t_c = t.ppf(p)
print(avg, sd, se, p, z_c)
#can only reject H0 if alpha is 0.1, not 0.05 or 0.01

#1.3
z_c = stats.norm.ppf(0.025)
se = (avg - 0.75) / z_c
n = (sd / se) **2
print(se, n)

#1.4
#H0: difference in means is 0
#H1: difference in means is not 0
#Use z-test

#1.5
avg0, sd0, se0, p0, z_c0 = getVals('eng0.txt')
avg1, sd1, se1, p1, z_c1 = getVals('eng1.txt')
z_c = (avg1 - avg0) / (se0 ** 2 + se1 ** 2) ** 0.5
p = 2*stats.norm.cdf(-z_c)
print(z_c, p)
#nearly 0 p-value which is lower than alpha 0.1, 0.05, 0.01 so the null hypothesis is rejected - significant difference between populations


#2.1
data = [3, -3, 3, 12, 15, -16, 17, 19, 23, -24, 32]
xbar = np.mean(data)
n = len(data)
sd = np.std(data, ddof=1)
t_c = stats.t.ppf(1 - (1 - 0.95)/2, n - 1)
high = -((t_c * sd / (n ** 0.5)) - xbar)
low = xbar + (t_c * sd / (n ** 0.5))
print(high, low)

t_c = stats.t.ppf(1 - (1 - 0.9)/2, n - 1)
high = -((t_c * sd / (n ** 0.5)) - xbar)
low = xbar + (t_c * sd / (n ** 0.5))
print(high, low)

t = (xbar - 0) / (sd / n**0.5)
p = 2 * stats.t.cdf(-abs(t), n-1)
print(p)