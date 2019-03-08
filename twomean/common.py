import math
"""
Calculate the degrees of freedom for two means using descriptive statistics.
"""
def t_test_df(s1mean, s1stdev, s1size, s2mean, s2stdev, s2size):
    return (((s1stdev**2)/(s1size)+(s2stdev**2)/(s2size))**2) / ((((s1stdev**2)/(s1size))**2)/(s1size-1) + (((s2stdev**2)/(s2size))**2)/(s2size-1) )

"""
Calculate the test statistic (real t-score) for two means using descriptive statistics.
"""
def t_test(s1mean, s1stdev, s1size, s2mean, s2stdev, s2size):
    return ((s1mean-s2mean)-(0))/(math.sqrt( (s1stdev**2)/(s1size) + (s2stdev**2)/(s2size)))