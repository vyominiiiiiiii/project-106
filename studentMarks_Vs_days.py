import csv
import plotly.express as px
import numpy as np

def plotFigure(dataPath):
    with open(dataPath) as csvFile:
        df=csv.DictReader(csvFile)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

def getDataSource(dataPath):
    marks=[]
    days=[]

    with open(dataPath) as csvFile:
        csvReader=csv.DictReader(csvFile)

        for row in csvReader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    
    return {"x":marks,"y":days}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation coefficient= ",correlation[0,1])

def setUp():
    dataPath="Student Marks vs Days Present.csv"
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
    plotFigure(dataPath)

setUp()
