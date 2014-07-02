import subprocess as suprocess

def popen_read(cmd):
    return subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE).communicate()[0]
