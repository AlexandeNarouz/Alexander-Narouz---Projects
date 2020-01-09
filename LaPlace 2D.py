
#Numerical Laplace Equation Solution with Finite Difference Method
#Solving electric potential in metal box

import numpy as np
from matplotlib import pyplot as plt

# Set maximum iteration
max_iterations = 500

def LaPlace_2D(n, top, bottom, left, right):
    '''This function will solve the 2D LaPlace equation for electric potential.
    Args:
        n: number of iterations
    Returns:
        V: potential as an array
    '''
    # Set Dimension and delta
    lenX = lenY = 20 #setting it to a box
    delta = 1

    # Boundary
    v_top = top
    v_bottom = bottom
    v_left = left
    v_right = right

    # Initial guess of interior grid
    v_guess = 0

    # Set colour interpolation and colour map
    colorinterpolation = 50
    colourMap = plt.cm.jet

    # Set meshgrid
    X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

    # Set array size and set the interior value with v_guess
    V = np.empty((lenX, lenY))
    V.fill(v_guess)

    # Set Boundary conditions
    V[(lenY-1):, :] = v_top
    V[:1, :] = v_bottom
    V[:, (lenX-1):] = v_right
    V[:, :1] = v_left

    # Iteration (We assume that the iteration is convergence)
    for iteration in range(0,n):
        for i in range(1, lenX-1, delta):
            for j in range(1, lenY-1, delta):
                V[i, j] = 0.25 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])
    return V

#Calling the function and assigning parameters for boundry conditions
vtop = 0
vbottom = 0
vleft = 30
vright = 0
V = LaPlace_2D(max_iterations,vtop,vbottom,vleft,vright)

# Configure the contour
plt.title("Electric Potential")
plt.contourf(X, Y, V, colorinterpolation, cmap=colourMap)

# Set Colorbar
plt.colorbar()

plt.show()



