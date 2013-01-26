import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from operator import itemgetter

here = os.path.dirname(os.path.abspath(__file__))
coltable = pd.read_csv(os.path.join(here,'Rcolortable.csv'),index_col=0)

def abline(intercept=0,slope=1):
    gca = plt.gca()
    default = gca.get_autoscale_on()
    gca.set_autoscale_on(False)
    gca.plot(gca.get_xlim(),gca.get_ylim())
    if default:
        gca.set_autoscale_on(default)
    # gca.set_aspect('equal','box')    
    # lim = ax.get_xlim()

class var2col:
    ## usage (discrete):
    ## vc=var2col(uniquevalues,col=colors) #or var2col(colorkey=colkey)
    ## vc.discrete(allvalues)
    ## or
    ## vc=var2col(uniquevalues) #selected by theme
    ## vc.colvec
    ## usage (continuous):
    ## vc=var2col(values)
    ## vc.colvec
    
    def __init__(self,x=None,n=None,theme=cm.jet,colors=None,colorkey=None):
        if type(n) is int:
            ## continuous
            ## possible values for n = 64, 256
            self.u = np.linspace(x.min(),x.max(),n+1)
            self.colors = theme(u/u.max(),1)
            self.index = zip(self.u[:-1],self.u[1:])
            self.colfn = self.continuous
        else:
            ## discrete
            if colorkey:
                x = map(itemgetter(0),colorkey)
                colors = map(itemgetter(1),colorkey)
            if colors:            
                self.u = x
                self.colors = coltable.ix[colors].values
            else:
                self.u = np.unique(x)
                self.colors = theme(np.arange(len(self.u))/float(len(self.u)),1)
            # import pdb; pdb.set_trace()
            self.cDFR = pd.DataFrame(self.colors,index=self.u)
            self.index = self.u if type(self.u) is list else self.u.tolist()
            self.colfn = self.discrete
        self.colvec = self.colfn(x)
        self.legend_obj = self.makelegend()
        
    def continuous(self,x):
        index = np.zeros(len(x))
        for i,b in enumerate(zip(self.u[:-1],self.u[1:])):
            within = np.logical_and(np.less_equal(b[0],x),np.less(x,b[1]))
            index[within] = i
        return self.colors[index]
    def discrete(self,x):
        return self.cDFR.ix[x].values

    def makelegend(self):
        h = []
        for c in self.colors.tolist():
            h.append(plt.Line2D(range(1), range(1), ls = '.', marker='o', color=c))
        return h

def cut(x,breaks,labels=None,right=False):
    if type(breaks) is int:
        breaks = np.linspace(*range(x)+[breaks])
    cmp = np.less_equal if right else np.less
    out = np.zeros(len(x))
    for i,b in enumerate(sorted(breaks,reverse=True)):
        out[cmp(x,b)] = i
    if labels:
        out = pd.Series(labels).ix[out]
    return out

def dev_list():
    import matplotlib
    figures = [manager.canvas.figure
               for manager in matplotlib._pylab_helpers.Gcf.get_all_fig_managers()]
    return figures

