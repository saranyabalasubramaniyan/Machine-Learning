# -*- coding: utf-8 -*-
"""
*             Name : Brth15to17_vs_poverty_Graph.py
*            Author: Saranya Balasubramaniyan (999901316)
*       Description: The program reads the csv file that contains data relevant to Location, 
*                    Poverty Percent, Birth 15 to 17, Birth 18 to 19, violence crime and teen birth.
*                    Birth 15 to 17 is marked in Y axis and Poverty Percent is marked in X axis
*                    for the scatter plot. A line for linear regression is also marked using the 
*                    values.This line can be used to predict the future values.
"""

import pandas as pd
import matplotlib.pyplot as plt 
from scipy import stats as st

#The csv name is assigned to the variable loc
loc = ("teen_birth_vs_poverty.csv")

#Reading the csv in location using Pandas method read_csv. The csv file has to be placed in
#the same location as the python file for the following line to read the csv file
dataFile = pd.read_csv(loc)

#Assigning the column with header PovPct to the variable xData
xData = dataFile["PovPct"]
#Assigning the column with header Brth15to17 to the variable Data
yData = dataFile["Brth15to17"]

#Using the lineregress method from scipy.stats
slope, intercept, r, p, std_err = st.linregress(xData, yData)

#Method calculate value multiplies the slope and the input argument
# and adds the intercept value. slope and intercept are global variable
def calculateVal(xVal):
  return slope * xVal + intercept

#graphmodel variable stores the list of values that are calculated for each value of 
#x-Axis in the method calculateVal
graphModel = list(map(calculateVal, xData))

#The matplotlib.pyplot, plt is used to create the scatter plot using the x and y data
#retrieved from the csv. The color of the plots are customized to red
plt.scatter(xData, yData, color='red')

#The plot method creates the lines regression line for the scattered plot data. 
plt.plot(xData, graphModel, color='green', linewidth='2')

#creates label for the axis, title and legend for the graph
plt.xlabel('Poverty Percent')
plt.ylabel('Birth-15to17')
plt.title("Brth15to17_vs_povertyPercent Graph")
plt.legend(['Fitted Line','Original Data'])
plt.show()