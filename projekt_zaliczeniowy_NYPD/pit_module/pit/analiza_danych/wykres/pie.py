import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

labels = ['dochody większe w 20','dochody większe w 19']

def pie(roznica_w_dochodach, podpis, labels = labels):
    plt.pie((roznica_w_dochodach['różnica dochodu z pit między 2019 a 2020']>0).value_counts(),labels=labels)
    plt.legend(loc = 'upper right')
    plt.title(podpis)
    fig = plt.gcf()
    fig.set_size_inches(15,15)
