def match(a,b):
    """
    returns (ordered) indices of b which contain values of a
    'None' if missing, which can be filtered with filter(None,result)
    length of result == length of a but with indices of b
    to find b corresponding to a, b[filter(None,match(a,b))]
    to find indices for a for which there is a match in b,
        a[[i for i,x in enumerate(match(a,b)) if x]]
    """
    return [b.index(x) if x in b else None for x in a]


def is_in(a,b):
    """
    tests which of a is in b
    """
    return [x for x in a if x not in b]    

def not_in(a,b):
    """
    tests which of a is not in b
    """
    return [x for x in a if x not in b]
