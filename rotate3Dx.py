import numpy
import math

def rotate_3Dx(theta):
    M = numpy.identity(4)
    M[1,1] = math.cos(math.radians(theta))
    M[2,2]= M[1,1]
    M[1,2]=-math.sin(math.radians(theta))
    M[2,1]=-M[1,2]

    return M






    # print(str(M[1,1]) + " " + str(M[1,2])
    # M = numpy.array(M)
    # print((M))
    # M = numpy.delete(M, 0, 0)
    # print("-----")
    # print(M)
    # print("-----")
    # print(M[numpy.ix_([0,1],[0,1])] )
