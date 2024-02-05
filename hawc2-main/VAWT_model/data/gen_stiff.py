"""
Script for creating st input files to HAWC2

This runs off of an assumption that the blades have an elliptical cross-section

For definitions and explanations of parameters, check How2HAWC document (page 25) 
and Section 2.2 of the HAWC2 E-course
"""

import math  

# Output file name 


# Enter parameters
m = 0.1             # mass per unit length [kg/m]
c = 0.15            # chord length [m]
w = 0.05            # width of blade [m] (same as the minor axis of the ellipse)
E = 10^9            # Young's modulus [Pa] 
G = 10^9            # shear modulus [Pa]
K = 1               # torsional stiffness constant at elastic center (0.5 for composites, higher for Euler-Bernoulli beam behavior)

# calculated parameters
a = c/2             # semi-major axis
b = w/2             # semi-minor axis
xm = 0
ym = 0
xs = 0
ys = 0
Ix = math.pi/4*a*b^3          # area moment of inertia in x (x is along major axis)
Iy = math.pi/4*b*a^3          # area moment of inertia in y (y is along minor axis)
rix = math.sqrt(Ix)           # radius of gyration along x (assuming constant mass density)
riy = math.sqrt(Iy)           # radius of gyration along y (assuming constant mass density)
kx = 1
ky = 1
A = math.pi*(c/2*w/2)         # cross-sectional area for an ellipse
thetaz = 0                    # structural pitch
xe = 0
ye = 0


