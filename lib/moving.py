import numpy as np
import pandas

def movingwindow(x,y=None,rangex=None,nbins=None,
                 increment=None,windowsize=None,
                 FUN=len):
    if y is None:
        y = x
    if rangex is None:
        rangex = [np.min(x),np.max(x)]
    if nbins is None:
        nbins = 100
    if increment is None:
        increment = np.diff(rangex)/nbins
    if windowsize is None:
        windowsize = increment*2
    alongx = np.arange(rangex[0],rangex[1],increment)
    values = np.zeros(len(alongx))
    select = lambda i: np.logical_and(x >= alongx[i]-windowsize/2.,\
                                      x <  alongx[i]+windowsize/2.)
    for i in range(len(alongx)):
        values[i] = FUN(y[select(i)])/windowsize
    return np.rec.fromarrays([alongx,values],
                             dtype=[('x','float'),('y','float')])

