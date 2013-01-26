Add to the top of each script file:
```python
import os
import sys
_mylib = os.path.expanduser('~/lib/python') # or os.path.join(os.environ['HOME'],'lib/python')
if _mylib not in sys.path:
    sys.path.append(_mylib)
```
The predicate statement guards against adding the same path multiple times if the code is run through the interpreter more than once. Alternatively, to add automatically:
```sh
export PYTHONPATH=$PYTHONPATH:~/lib/python
```
Explicit is generally preferred in python, but as long as each module within `lib/python` is added, it should also be acceptable.

To reload edited modules, use `reload(module_name)` rather than `import module_name`.
