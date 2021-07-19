import plotly.express as px
import csv
import numpy as np
def plotFigure(datapath):
    with open(datapath)as f :
        df=csv.DictReader(f)
        fig=px.scatter(df,x='Coffee',y='sleep in hours')
        fig.show()
def getDataSource(datapath):
    Coffee=[]
    hoursofsleep=[]
    with open(datapath) as f :
        csvreader=csv.DictReader(f)
        for row in csvreader:
            hoursofsleep.append(float(row['sleep in hours']))
            Coffee.append(float(row['Coffee']))
    return{'x':hoursofsleep,'y':Coffee}
def findCorelation(datasource) :
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation between Coffee vs sleep in hours:- \n--->",correlation[0,1])
       
def setup () :
    datapath='./cups of coffee vs hours of sleep.csv'
    datasource=getDataSource(datapath)
    findCorelation(datasource)
    plotFigure(datapath)
setup()

    