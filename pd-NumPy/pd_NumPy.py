import numpy as np

def stats(dir = "data/iris.csv" ):
    data = np.loadtxt(dir ,delimiter=',', usecols=(0,1,2,3), skiprows=1)
    score = [np.median(data, axis=0),
             np.std(data, axis=0),
             np.mean(data, axis=0)]

    score = np.array(score)
    return score