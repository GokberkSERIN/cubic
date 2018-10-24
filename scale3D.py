import numpy



def scale_3D(scalex,scaley,scalez):
    M = numpy.identity(4)
    M[0,0] = scalex
    M[1, 1] = scaley
    M[2, 2] = scalez
    return(M)
