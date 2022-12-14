#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ret = fct(*args)
        return ret
    except Exception as e:
        print("Exception: {0}".format(e), file=sys.stderr)
        return None
