import csv


def save(score):
    # open the file in the write mode
    f = open('iris_analisys/score.csv', 'w', newline = '')

    # create the csv writer
    writer = csv.writer(f)
    print(score)

    labels = ['mean', 'stdev', 'median']
    writer.writerow(labels)
    # write a row to the csv file
    for i in range(len(score)):
        writer.writerow(score[i])

    # close the file
    f.close()