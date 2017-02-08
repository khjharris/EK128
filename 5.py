id = {"name":"Kenwood Harris", "buname":"khjr"}

import numpy as np
import math
import matplotlib.pyplot as plt

def do_steps(N,D,T_initial):
    values = {} #Sets up the values dicitonary with the step number as the key and the value as the np array
    values[0] = T_initial       #Step 0 is the original T_initial

    for i in range(1,N+1):        #Loops for the correct number of steps
        values[i] = np.zeros(len(T_initial))        #Sets up the values in the np array as an np array with zeros for easy appending
        for x in range(0,len(T_initial)):           #Loops through all the positions in the np array

            if x == 0:  # If the value is the first value in the np array
                firstval = values[i-1][x+1]
                secondval = values[i-1][x]
                thirdval = firstval - secondval
                delta = thirdval * D
                values[i][x] = values[i-1][x] + delta

            elif x == len(T_initial)-1:     # if the value is the last value in the np array
                firstval = values[i-1][x-1]
                secondval = values[i-1][x]
                thirdval = firstval - secondval
                delta = thirdval * D
                values[i][x] = values[i-1][x] + delta

            else:       #For all the interior points in the np arrray
                firstval = values[i-1][x+1]
                secondval = values[i-1][x]
                thirdval = firstval - secondval
                fourthval = thirdval * D
                fithval = values[i-1][x-1]
                sixthval = fithval - secondval
                seventhval = sixthval * D
                delta = fourthval + seventhval
                values[i][x] = values[i-1][x] + delta

    return values[N]

def stats(T):
    return (np.mean(T), np.std(T))  #Simply returns the mean and the standard deviation as a tuple

def sim(N,D,T):
    x = np.linspace(0.0,N,N)    #Creates an aray with evenly spaced x values N times across N
    y = np.zeros(N)     #Creates an empty zeros array for the standard deviation

    for i in range(0,len(y)):
        y[i] = stats(do_steps(i,D,T))[1]    #appends the standard deviations for each step at their respctive points

    plt.plot(x,y)   #plots x against y
    plt.show()

"""
The following runs the simulation for the case given
"""

TA=np.zeros(51)
TA[25] = 10
sim(1000,0.01,TA)
