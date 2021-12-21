import numpy as np
import pandas as pd
from pathlib import Path
import os



def iris_to_excel(dir = "data/iris.csv", new_dir = "data/iris2.xlsx"):
    # this function puts rows of iris datest with the same variety into same excel sheet
    iris = pd.read_csv(dir)
    varieties = iris["variety"].unique().tolist()

    #checking if excel file exists, if exists clear this file, else create file
    if os.path.isfile(new_dir):
        os.remove(new_dir)
        open(new_dir,'w')
    else:
        open(new_dir, 'w')

    # writing varieties into different excel sheet
    with pd.ExcelWriter(new_dir, mode='w') as writer:
        for i in range(len(varieties)):
                df = iris[iris["variety"]==varieties[i]]
                df.to_excel(writer, sheet_name= varieties[i])


iris_to_excel()                



