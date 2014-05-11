from __future__ import division
from numpy import *

#Inputting features and number of data sets
F = input("\nNumber of Observed Features: ")
F = F + 1
N = input("\nNumber of Data Sets: ")
i = 0;
y = {}
a = [1]
#getting data sets from user and storing in array X 
while( i<N ):
    j = 1;
    k = 1;
    while ( k<len(a) and i!=0 ):
        del a[k]
    while ( j<F ):
            f = input("\nEnter feature value: ")
            a.insert(j, f)
            j = j + 1
    if ( i == 0):
            X = array(a)

    else :
            X = vstack((X, a))
    y[i] = input("\nEnter output: ")
    i = i + 1
#storing output to Y
k = 0
Y = []
while( k<N ):
    Y = hstack((Y, y[k]))
    k = k + 1
#Calculation of B
B = []
C = X.transpose()
D = dot(C, X)
#inverting X adn Xtrans
from numpy.linalg import inv
E = inv(D)
M = dot(E, C)
B = dot(M, Y)
print "Coeffecient Values: "
print B
S = dot(X, B)
k = 0
print "Predicted value based on our B value:"
while ( k<len(T) ):
    print T[k]
    k = k + 1
# getting value of sum of sqaure of difference
e = Y - S
k = 0
SSR = 0
import math

while ( k<len(e) ):
    sqr = e[k] * e[k]
    SSR = SSR + sqr
    k = k + 1
num = N - 2
sigma = sqrt(SSR / num)
#getting average of Y
k = 0
tsum = 0
while ( k<len(Y) ):
    tsum = tsum + Y[k]
    k = k + 1
avg = tsum / len(Y)
#finding the sqaure of difference between Y and avg
k = 0
tdiff = 0
SST = 0
while ( k<len(Y) ):
    tdiff = Y[k] - avg
    tsqr = tdiff * tdiff
    SST= SST + tsqr
    k = k + 1
# finding R sqaure
temp = SSR / SST
Rsqr = 1 - temp
R = sqrt(Rsqr)
print "R square: "
print Rsqr
#Applying model to new datas
n = input("\n\n\nEnter number of values to be predicted: ")
i = 0;
a = [1]
#Getting new input datas
while ( i<n ):
    j = 1;
    k = 1;
    while ( k<len(a) and i!=0 ):
        del a[k]
    while ( j<F ):
            f = input("\nEnter feature: ")
            a.insert(j, f)
            j = j + 1
    print a
    if ( i == 0):
            R = array(a)
    else :
            R = vstack((R, a))
    i = i + 1
T = dot(R, B)
#Output of values
k = 1
print "Predicted values of new set: "
while ( k<len(T) ):
    print T[k]
    k = k + 1

