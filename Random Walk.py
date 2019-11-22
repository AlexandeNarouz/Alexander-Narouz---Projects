# This code will simulate a random walk in 1D 2D and 3D and find the diffusion constant for each dimension

import random
import math
import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize

def random_walk1D(n):
    '''This function will simulate a random walk in one dimension where the walker will take random steps of length
    1 and -1 along a line. The function finds a random number between 0 and 1 and depending on the value of the number 
    the walker will walk in the +1 or -1 direction. The squared position will be recorded in a list named displacement.
    Args:
        n: number of steps the walker will take
    Returns:
        Returns list of position squared at each step
    '''
    count = 0
    count_sum = 0
    displacement = []
    for i in range(n):
        random_int = random.random()
        if random_int > 0.5:
            count = 1
        if random_int <= 0.5:
            count = -1
        count_sum += abs(count**2)
        displacement.append(count_sum)
    return displacement    

def average(func,n): #n is number of walkers
    '''This function will calculate the average of the position squared for n, number of walkers. It will convert the
    list of displacements into an array and sum them together n amount of times. Then it will divide the array by the 
    number of walkers which results in an array for the average of the displacement squared.
    Args:
        func: function we wish to calculate the average displacement for. Can be either 1D, 2D or 3D walk function.
        n: number of walkers
    Returns:
        The average displacement squared for n number of walkers as an array.
    '''
    total = np.zeros(len(func(100)))
    result = []
    for i in range(n):
        array = np.array(func(100))
        total = array + total
    ans = total / n
    return ans

def model(s,param):
    '''This function takes the number of steps and a guessing paramater to solve the equation <x**2> = D*s It
    will be used to fit a line to the displacement squared values.
    Args:
        s: number of steps
        param: Guessing parameter that will be equal to the diffusion constant D.
    Returns:
        param * s as a foat
    '''
    return param*s

def random_walk2D(n):
    '''This function will simulate a random walk in 2 dimensions using polar coordinates to determine total 
    displacement of the walker. The function calculates radius in the x and y direction by finding a random number 
    between 0 and 1 then it calculates theta for the x and y components by finding a random number between 0 and 360.
    x and y displacement is calculated using polar to cartestian conversions. The total displacement squared is 
    calculated using pythagorean theorm. The values for the total displacement squared are stored in a list for each step.
    Args:
        n: number of steps
    Returns:
        displacement squared at each step as a list
    '''
    displacement = []
    total_displacement_squared = 0
    for i in range(n):
        #x components
        r_x = random.random()
        theta_x = random.randint(0,360)
        x_component = r_x * np.cos(math.radians(theta_x))
        # y components
        r_y = random.random()
        theta_y = random.randint(0,360)
        y_component = r_y * np.sin(math.radians(theta_y))
        total_displacement_squared += (x_component**2 + y_component**2)
        displacement.append(total_displacement_squared)
    return displacement

def random_walk3D(n):
    '''This function will simulate a random walk in 3 dimensions using spherical coordinates to determine total displacement 
    of the walker. The function calculates radius in the x and y direction by finding a random number between 0 and 1
    then it calculates theta and phi for the x, y, and z components by finding a random number between 0 and 360. 
    x and y displacement is calculated using spherical to cartestian conversions. The total displacement squared 
    is calculated using pythagorean theorm. The values for the total displacement squared are stored in a list for each step.
    Args:
        n: number of steps
    Returns:
        Displacement squared as a list
    '''
    displacement = []
    total_displacement_squared = 0
    for i in range(n):
        #x components
        r_x = random.random()
        theta_x = random.randint(0,360)
        phi_x = random.randint(0,360)
        x_component = r_x * np.cos(math.radians(theta_x)) * np.sin(math.radians(phi_x))
        # y components
        r_y = random.random()
        theta_y = random.randint(0,360)
        phi_y = random.randint(0,360)
        y_component = r_y * np.sin(math.radians(theta_y)) * np.sin(math.radians(phi_y))
        #z components
        r_z = random.random()
        phi_z = random.randint(0,360)
        z_component = r_z * np.cos(math.radians(phi_z))
        total_displacement_squared += (x_component**2 + y_component**2 + z_component**2)
        displacement.append(total_displacement_squared)
    return displacement

#calling 1D random walk for 2 walkers
oneD_average = average(random_walk1D,2)
step = np.linspace(1,100,100)

#fitting curve to data and finding slope for 1D
popt, pcov = optimize.curve_fit(model,step,oneD_average,[0.])

#print slope for 1D
slope_1D = popt
print("The diffusion constant for 1D walk is : {}".format(slope_1D))

#plotting <x**2> vs n for 1D
plt.xlabel("n (steps)")
plt.ylabel("<x**2>")
plt.plot(step,oneD_average,'o', label = 'Random Walk in 1D')
plt.plot(step, model(step,popt[0]), linewidth = 4, label = '')
plt.legend()
plt.savefig('Random_Walk_1D.png')
plt.show()

# Calling 2D random walk for 2 walkers
twoD_average = average(random_walk2D,2)
step_2D = np.linspace(1,100,100)

#fitting curve for 2D
popt, pcov = optimize.curve_fit(model,step,twoD_average,[0.])

#print slope for 2D
slope_2D = popt
print("The diffusion constant for 2D walk is : {}".format(slope_2D))

#Plotting <x**2> vs n for 2D    
plt.xlabel("n (steps)")
plt.ylabel("<x**2>")
plt.plot(step_2D,twoD_average, 'o', label = 'Random Walk in 2D')
plt.plot(step_2D, model(step,popt[0]), linewidth = 4, label = '')
plt.legend()
plt.savefig('Random_Walk_2D.png')
plt.show()

#Calling 3D random walk for 2 walkers
threeD_average = average(random_walk3D,2)
step_3D = np.linspace(1,100,100)

#curve fitting for 3D
popt, pcov = optimize.curve_fit(model,step,threeD_average,[0.])

#print slope for 3D
slope_3D = popt
print("The diffusion constant for 3D walk is : {}".format(slope_3D))

#plotting <x**2> vs n for 3D
plt.xlabel("n (steps)")
plt.ylabel("<x**2>")
plt.plot(step_3D,threeD_average, 'o', label = 'Random Walk in 3D')
plt.plot(step_3D, model(step,popt[0]), linewidth = 4, label = '')
plt.legend()
plt.savefig('Random_Walk_3D.png')
plt.show()

