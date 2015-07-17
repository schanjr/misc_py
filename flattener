def flatten(*args):
    output = []
    for arg in args:
        if hasattr(arg, '__iter__'):
            output.extend(flatten(*arg))
        else:
            output.append(float(arg))
    s = sorted(output)
    return s
