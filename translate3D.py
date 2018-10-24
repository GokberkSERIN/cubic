import numpy




def translate_3D(x,y,z):
    M = numpy.identity(4)
    M[0,3] = x
    M[1, 3] = y
    M[2, 3] = z
    return(M)