"""
Author: Nirmal Kumar
E-Mail: s9nirama@stud.uni-saarland.de
Description: Code for whitening the data obtained from 
"https://archive.ics.uci.edu/ml/datasets/Airfoil+Self-Noise"
"""

import numpy as np

x = np.empty([1503, 6])
with open('airfoil_self_noise.dat', 'r') as _fileRead:
    lines = _fileRead.readlines()
    i = 0
    for line in lines:
        _temp = line.split('\t')
        #import ipdb; ipdb.set_trace()
        x[i] = np.array([float(_temp[0]),
                    float(_temp[1]),
                    float(_temp[2]),
                    float(_temp[3]),
                    float(_temp[4]),
                    float(_temp[5])])
        i += 1

print(x.shape)
# this for loop performs
# mean centering of data
for i in range(x.shape[1]-1):
    x[:,i] -= np.mean(x[:,i])

# this for loop makes each data point
# a unit vector
for i in range(x.shape[0]):
    x[i,:5] /= np.linalg.norm(x[i,:5])

with open('dataset.csv', 'w') as _fileWrite:
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            _fileWrite.write(repr(x[i,j]))
            if j < 6:
                _fileWrite.write(',')
        _fileWrite.write('\n')
