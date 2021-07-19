import plotly.express as px
import csv
import numpy as np
def plotFigure(datapath):
    with open(datapath)as f :
        df=csv.DictReader(f)
        fig=px.scatter(df,x='Temperature',y='Ice-cream Sales')
        fig.show()
def getDataSource(datapath):
    IcecreamSales=[]
    Temperature=[]
    with open(datapath) as f :
        csvreader=csv.DictReader(f)
        for row in csvreader:
            IcecreamSales.append(float(row['Ice-cream Sales']))
            Temperature.append(float(row['Temperature']))
    return{'x':IcecreamSales,'y':Temperature}
def findCorelation(datasource) :
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print("Correlation between Temperature vs Ice Cream Sales :- \n--->",correlation[0,1])
       
def setup () :
    datapath='./cups of coffee vs hours of sleep.csv'
    datasource=getDataSource(datapath)
    findCorelation(datasource)
    plotFigure(datapath)
setup()
