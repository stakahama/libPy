import io
import pandas
import numpy as np

def read_orgtable(filename,header=True):
    with open(filename) as f:
        out = []
        for line in f:
            if '|-' == line[:2]:
                continue
            out.append(map(str.strip,line.strip().strip('|').split('|')))
    if headers:
        names = out[0]
        rest = out[1:]
    else:
        names = False
        rest = out
    fobj = io.BytesIO('\n'.join(map('\t'.join,rest)))
    recarr = np.genfromtxt(fobj,dtype=None,delimiter='\t',names=names)
    return pandas.DataFrame(recarr)
