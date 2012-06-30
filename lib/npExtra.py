import numpy as np
import numpy.lib.recfunctions as recfn

def unstructure(x):
    return x.view(x.dtype[0]).reshape(x.shape[0],-1)

def cbind(a,b,FUN='rec_append_fields'):
    """
    append_fields compatible with masks
    """
    dt = b.dtype
    if not dt.names:
        print 'b is not a structured array'
        return a
    appendf = getattr(recfn,FUN)
    return appendf(a,dt.names,
                   [b[x] for x in dt.names],
                   [x[1] for x in dt.descr])

def getdtypes(d):
    return [x[1] for x in d.descr]
