import csv
import numpy as np


def getDataSource(data_path):
    Coffee_in_ml = []
    Sleep_in_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            Sleep_in_hours.append(float(row["Sleep in hours"]))

    return {"x" : Coffee_in_ml, "y": Sleep_in_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between coffee in ml and sleep in hours :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Coffee in ml vs sleep in hours.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()