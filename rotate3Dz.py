import numpy
import math



def rotate_3Dz(theta):
    M = numpy.identity(4)
    M[0,0] = math.cos(math.radians(theta))
    M[1,1]= M[0,0]
    M[0,1]=-math.sin(math.radians(theta))
    M[1,0]=-M[0,1]

    return(M)

