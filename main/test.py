import numpy
import bitarray

with open('shape.npy', 'rb') as fh:
    shape = numpy.load(fh)
    print(shape[:-1])

