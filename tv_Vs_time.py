import csv
import plotly.express as px
import numpy as np

def plotFigure(dataPath):
    with open(dataPath) as csvFile:
        df=csv.DictReader(csvFile)
        fig=px.scatter(df,x="Size of TV",y="\tAverage time spent watching TV in a week (hours)")
        fig.show()

def getDataSource(dataPath):
    sizeOfTv=[]
    averageTimeSpent=[]

    with open(dataPath) as csvFile:
        csvReader=csv.DictReader(csvFile)

        for row in csvReader:
            sizeOfTv.append(float(row["Size of TV"]))
            averageTimeSpent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    
    return {"x":sizeOfTv,"y":averageTimeSpent}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation coefficient= ",correlation[0,1])

def setUp():
    dataPath="Size of TV and time spent.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)

setUp()
