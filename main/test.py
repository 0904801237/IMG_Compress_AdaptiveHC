import numpy
import bitarray

a = bitarray.bitarray("110011")
del a[1:1+3]
print(a)