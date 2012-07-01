Add with

    import os
    import sys
    _mylib = os.path.join(os.environ['HOME'],'lib/python')
    if _mylib not in sys.path:
        sys.path.append(_mylib)

at the top of each .py file, or in .profile with 

    export PYTHONPATH=$PYTHONPATH:~/lib/python

to load automatically. Of course, the former is preferred.
