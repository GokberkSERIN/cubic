import numpy
import math



def rotate_3Dy(theta):
    M = numpy.identity(4)
    M[0,0] = math.cos(math.radians(theta))
    M[2,2]= M[0,0]
    M[0,2]=-math.sin(math.radians(theta))
    M[2,0]=-M[0,2]

    return(M)