from __future__ import division
from collections import Counter
from src.TURTLE.linear_algebra import sum_of_squares, dot
from math import sqrt

"""
Define the mean: The mean represent the division between the sum of the given data points and the
number of data points.

The mean is *very* sesitive to outliners.

mean(x) -> will compute the mean of x.
"""
def mean(x):
    return sum(x)/len(x)

"""
Define the median: The median represent the middle-most value(if the number of data points is odd)
or the average of the two middle-most values(if the number of data points is even).

The median is not as sensitive to outliners as the mean. 

median(x) -> will compute the median of x 
"""
def median(x):
    n = len(x) 
    sorted_x = sorted(x)
    midpoint = n//2
    
    if n%2 == 1:
        # if odd, return the middle value
        return sorted_x[midpoint]
    else:
        return (sorted_x[midpoint-1] + sorted_x[midpoint])/2

"""
Define the Quantile: Quantile is a generalization of median. A quantile represents the value less than
which a certain percentile of the data lies. Median is a quantile with the percentile of 50%

quantile(x,p) -> computes the quantile for the data points stored in x which lies under the p percentile.
i.e. returns the exact value found at the p-th part of x

The value of p must be the form of 0.something. E.g. for 20% => p=0.2

DO NOT USE THIS FUNCTION IF YOU WANT YOUR P TO BE 50%. INSTEAD USE meadian(x).
"""
def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

"""
Define mode: The mode represents the most common value/values from the given data points.

mode(x) -> will compute the mode of x
"""
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count==max_count]

"""
Dispersion refers to measures of how spread out our data is. Typically they'restatistics for
which **values near zero signify not spread out at all** and for which **large values signify
very spread out**.

The rest of the implemented functions below represent methods of analyzing dispersion in data sets.
"""

"""
Define range: The range is a form of dispersion method which tells us what is the difference between max(x) and
min(x). As we can imagine, range is very sensitive if we have large outliers as the min(x) or max(x).

data_range -> returns max(x)-min(x)
"""
def data_range(x):
    return max(x)-min(x)

"""
Define de_mean: The de_mean function just subtracts from every data point the mean of the sample. The new set
of datapoints will have the mean equal with 0.

de_mean(x) -> will return an array with the new elements
"""
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

"""
Define variance: The variance is a more complex dispersion method which the average squared eviation from the mean,
except we are dividing by n-1 instead of n because we deal with a sample, not the entire population. In fact, x_bar
is just an estimate of the actual mean, which means that on average (x_i - x_bar) ** 2 is an underestimate of x_i's
squared deviation from the mean, which is why we divide by n-1 instead of n.

The variance for entire population(which is also known as standard deviation):
σ² = Σ(xᵢ - μ)² / n
    where:
    σ² = variance
    xᵢ = each value in the dataset
    μ = mean of the dataset
    n = number of values

The variance for a sample:
s² = Σ(xᵢ - x_bar)² / (n-1)
    where:
    s² = sample variance
    xᵢ = each value in the sample
    x_bar = mean of the sample
    n = number of values

variance(x) -> will compute the variance of the given *sample*
"""
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n-1)

"""
Define standard deviation: It is harder to interpret the result of variance because of it's squared nature, we will
use standard_deviation as the square root of variance.

Both standard_deviation and data_range have the same problem with outliers.

standard_deviation(x) -> the square root of variance
"""
def standard_deviation(x):
    return sqrt(variance(x))

"""
Define interquartile_range: Because data_range has a high sensitivity when it comes to outliers, we introduce the
interquartile_range which is the differente of quantile(x,0.75) and quantile(x,0.25).

interquartile_range(x) -> return the difference between the 75th element and 25th element from a sorted order
"""
def interquartile_range(x):
    return quantile(x,0.75) - quantile(x,0.25)

"""
Correlation refers to methods that show how correlate is the data.

The following methods lies under the umbrella of correlation techniques.
"""

"""
Define covariance: Covariance is a correlation method which measures how two variables vary in tandem from their
mean.

Sample Covariance formula:
cov(X,Y) = Σ((xᵢ - x_bar)(yᵢ - y_bar)) / (n-1)
    where:
    xᵢ = each value in dataset X
    yᵢ = each value in dataset Y
    x_bar = mean of dataset X
    y_bar = mean of dataset Y
    n = number of paired observations

possible values:
0 -> indicates no linear correlation
positive covariance -> is a large value=> x tends to be large when y is large and is a small value=> x tends to be large
when y is small
negative covariance -> is a large value=> x tends to be small when y is large and is a small value=> x tends to be small 
when y is small

It is hard to look at covariance because:
    - its units are the product of the inputs units
    - if each user had twice as many friends the covariance would be twice as large

covariance(x,y) -> compute the covariance of x,y 
"""
def covariance(x,y):
    n = len(x)
    return dot(de_mean(x), de_mean(y))/(n-1)

"""
Define correlation: is a method which divides out the standard deviations of both variables. The correlation is unitless
and always lies between -1(perfect anti-correlation) and 1(perfect corrlation). For example 0.25 represents a relatively weak
positive correlation.

Pearson Correlation Coefficient formula:
ρ = covariance(X,Y) / (σₓ * σᵧ)

Expanded form:
ρ = Σ((xᵢ - x_bar)(yᵢ - y_bar)) / √[Σ(xᵢ - x_bar)² * Σ(yᵢ - y_bar)²]
    where:
    ρ = correlation coefficient
    covariance(X,Y) = covariance of X and Y
    σₓ = standard deviation of X
    σᵧ = standard deviation of Y
    xᵢ = each value in dataset X
    yᵢ = each value in dataset Y
    x_bar = mean of dataset X
    y_bar = mean of dataset Y

correlation(x,y) -> compute the correlation between the numbers means
"""
def correlation(x,y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x,y)/stdev_x/stdev_y
    else:
        return 0