import pandas as pd
from scipy.integrate import cumtrapz
import matplotlib.pyplot as plt
import numpy as np


#Returns the "height" of the normal function of the given parameters at the point x relative to the mean
def normalHeight(x,mean,dev):
    return (1/(np.sqrt(2*np.pi*(dev**2))))*np.exp(-0.5*(((x-mean)/dev)**2))

#Our parameters for the conference
openingTime = 8
closingTime = 17
step = 0.01
peakprod = 12
shape = 4

x = np.arange(openingTime, closingTime, step)

df = pd.read_csv("world_cities_modified.csv")

print(df)

cols = [1,10,12]
gmtdf =  df[df.columns[cols]]

print(gmtdf)

gmtdf['gmtOffset'] = gmtdf['gmtOffset'].divide(60)

#for value in gmtdf['gmtOffset']:
#    print(value)

attendees = ((6,100),(5,1),(5,2))

#print(df)

#print(df.iloc[1])

bestCity = ""
bestScore = 0

for index, city in gmtdf.iterrows():
    sumScore = 0
    for attendee in attendees:
        sumScore += attendee[1]*np.trapz(normalHeight(x,peakprod-attendee[0]+city['gmtOffset'],shape), x)
        if sumScore > bestScore:
            bestScore = sumScore
            bestPop = city['population']
            bestCity = city['city']+" at gmt:"+str(city['gmtOffset'])
        if sumScore == bestScore:
            if city['population'] > bestPop:
                bestScore = sumScore
                bestPop = city['population']
                bestCity = city['city']+" at gmt:"+str(city['gmtOffset'])

print(bestCity)
print("Population: "+str(bestPop))
print("Score: "+str(bestScore))
