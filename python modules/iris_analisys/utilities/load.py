import csv
# defeault
txt_file_dir = "C:/Users/cezar/OneDrive/Pulpit/Studia/vscode-programy/python/NYPD/Nowy folder/iris_analisys/utilities/iris.csv"

def load():
    with open("C:/Users/cezar/OneDrive/Pulpit/Studia/vscode-programy/python/NYPD/Nowy folder/iris_analisys/utilities/iris.csv", newline='') as csvfile:
        iris = csv.reader(csvfile)
        iris_arr = []
        
        iterator = iter(iris)

        for row in iterator:
            iris_arr.append(row)
            break
        
        for row in iterator:
            for i in range(len(row)-1):
                row[i] = float(row[i])
            iris_arr.append(row)
    #print(iris_arr)
    return iris_arr

load()

