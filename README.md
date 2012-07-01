Add to the top of each script file:

    import os
    import sys
    _mylib = os.path.join(os.environ['HOME'],'lib/python') # or os.path.expanduser('~/lib/python')
    if _mylib not in sys.path:
        sys.path.append(_mylib)

(I often rerun the preamble if I am modifying a library so the predicate statement guards against adding the same path multiple times.) Alternatively, to add automatically:

    export PYTHONPATH=$PYTHONPATH:~/lib/python

Explicit is generally preferred in python, but as long as each module within lib/python is added, it should also be acceptable.
