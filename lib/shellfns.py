

def popen_read(cmd):
    import subprocess as spr
    return spr.Popen(cmd,shell=True,stdout=spr.PIPE).communicate()[0]
