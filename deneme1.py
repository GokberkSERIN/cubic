degisken = "asd"
degisken = 1

satir=0
sutun=0
matris=[]

from scipy import mat
from matplotlib import pyplot
from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from rotate3Dx import rotate_3Dx
from rotate3Dy import rotate_3Dy
from rotate3Dz import rotate_3Dz
from scale3D import scale_3D
from translate3D import translate_3D
import math
import numpy

cube = mat('[-0.5, -0.5, -0.5, -0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5; -0.5, -0.5, 0.5, 0.5, -0.5, -0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5 0.5, 0.5, 0.5 0.5; 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0; 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]')
vroll=math.radians(0.0)
vpitch=math.radians(0.0)
vyaw=math.radians(0.0)

gbase=rotate_3Dz(vroll)*rotate_3Dy(vpitch)*rotate_3Dx(vyaw)

bsx=720
bsy=720
bsz=200

bscale=scale_3D(bsx,bsy,bsz)
base=gbase*bscale*cube


temp_matrix = numpy.array(base)

x = temp_matrix[0, :]
y = temp_matrix[1, :]
z = temp_matrix[2, :]

# x = base[0, ]

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y, z, zdir='z', label='zs=0, zdir=z')

plt.show()




# deneme = rotate_3Dx(30)
# print(deneme)
# print ("--*--")
# print(rotate_3Dy(30))
# print ("----")
# print(rotate_3Dz(30))
# print ("----")
# print(scale_3D(20,20,20))
# print ("--*--")
# print(translate_3D(20,30,50))




# print(A )
#
# print(math.sin(math.radians(30)))
#
# print(math.pi)
#
# n=int(input("enter a number"))
# for i in range(1,n):
#     for j in range (1,n):
#         if (i==j):
#             print ("1",sep=" ", end=" ")
#         else:
#             print("0",sep=" ",end=" ")
#     print()