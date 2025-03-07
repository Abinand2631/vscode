def triple_decor(fun):
    def wrapper(n):
        any_list=fun(n)
        return [item*3 for item in any_list]
    return wrapper



@triple_decor
def reverse_list(l):
    return l[::-1]
@triple_decor
def upper_list(l):
    return [item.upper() for item in l]
@triple_decor
def fibonacci(n):
    result =[]
    a,b=0,1
    while b<=n:
        result.append(a)
        a,b=b,a+b
    return result
print(reverse_list([1,2,3,4]))
print(upper_list(['a','b','c']))
print(fibonacci(6))