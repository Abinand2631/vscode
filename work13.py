def upper_decor(fun):
    def wrapper(n):
        result=fun(n)
        return result.upper()
    return wrapper
def al_d(fun):
    def wrapper(sent):
        result=fun(sent)
        length=len(result)
        result += str(length)
        return result
    return wrapper
@al_d
@upper_decor
def h_n(name):
    return 'hello '+name
print(h_n('dheeraj '))