import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import numpy as np
import pandas

def abline(intercept=0,slope=1):
    gca = plt.gca()
    gca.set_autoscale_on(False)
    gca.plot(gca.get_xlim(),gca.get_ylim())
    # gca.set_aspect('equal','box')    
    # lim = ax.get_xlim()

class var2col:
    
    def __init__(self,x,n=None,theme=cm.jet):
        if type(n) is int:
            ## continuous
            ## possible values for n = 64, 256
            self.u = np.linspace(x.min(),x.max(),n+1)
            self.colors = theme(u/u.max(),1)
            self.index = zip(self.u[:-1],self.u[1:])
            self.colfn = self.continuous
        else:
            ## discrete        
            self.u = np.unique(x)
            self.colors = theme(np.arange(len(self.u))/float(len(self.u)),1)
            self.cDFR = pandas.DataFrame(self.colors,index=self.u)
            self.index = self.u.tolist()
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
