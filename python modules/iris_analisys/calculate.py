"""
This module runs the analisys of iris dataset
"""
import statistics
from iris_analisys.utilities import load

def calculate():
    iris = load()
    rows = len(iris)
    columns = len(iris[0])
    score = [[],[],[],[]]
    for i in range(columns-1): # iterate every column, besides last one (beacuase its string type)
        x=[]
        
        for j in range(1, rows):
            x.append(iris[j][i])
        
        #mean 
        score[i].append(statistics.mean(x))
        #stdev
        score[i].append(statistics.stdev(x))
        #median
        score[i].append(statistics.median(x))
        """"
        print(f"its mean for {iris[0][i]} column: {score[i][0]}")
        print(f"its stdev for {iris[0][i]} column: {score[i][1]}")
        print(f"its median for {iris[0][i]} column: {score[i][2]}")
        print("\n")
        """
        #print(score)
    return score

calculate()