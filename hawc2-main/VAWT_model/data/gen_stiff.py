"""
Script for creating st input files to HAWC2

This runs off of an assumption that the blades have an elliptical cross-section

For definitions and explanations of parameters, check How2HAWC document (page 25) 
and Section 2.2 of the HAWC2 E-course
"""

import math  
from _functions import make_hawc2_st_array, save_h2_st_arr

# Output file name 
fileName = 'tower_stiff.st'

# generate array
st_array = make_hawc2_st_array(1, 0.019, 0.003, 205e9, 80e9, 7850, 1)

# create file! 
save_h2_st_arr(fileName, st_array, 'towertop', notorsion = False, rigid = True)


# Below here is outdated, for when we wanted to create our own st generation script. The formulas are still good tho

# # Enter parameters for blade
# m_b = 1.5/2           # mass per unit length [kg/m]
# c_b = 0.15            # chord length [m]
# E_b = 10^9            # Young's modulus [Pa] 
# G_b = 10^9            # shear modulus [Pa]
# K_b = 1               # torsional stiffness constant at elastic center (0.5 for composites, higher for Euler-Bernoulli beam behavior)

# # calculated parameters for blade
# w_b = 0.18*c_b          # width of blade [m] (same as the minor axis of the ellipse) (NACA0018 means width is 18% of chord length)
# a_b = c_b/2             # semi-major axis
# b_b = w_b/2             # semi-minor axis
# xm_b = 0                # x location of mass center (for objects with two axes of symmetry like ellipses, xm=xs=xe=0)
# ym_b = 0                # y location of mass center
# xs_b = 0                # x location of shear center
# ys_b = 0                # y location of shear center
# Ix_b = math.pi/4*a_b*b_b^3          # area moment of inertia in x (x is along major axis)
# Iy_b = math.pi/4*b_b*a_b^3          # area moment of inertia in y (y is along minor axis)
# rix_b = b_b/2           # radius of gyration along x (assuming constant mass density)
# riy_b = a_b/2           # radius of gyration along y (assuming constant mass density)
# kx_b = 1
# ky_b = 1
# A_b = math.pi*(c_b/2*w_b/2)         # cross-sectional area for an ellipse
# thetaz_b = 0                    # structural pitch
# xe_b = 0                # x location of elastic center
# ye_b = 0                # y location of elastic center


