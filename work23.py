"""q=[1,2,3,3,4]
def multiply(n):
    return n*2
w=list(map(multiply,q))
print(w)
"""
try:
    n1=int(input("first :"))
    n2=int(input("second :"))
    sum=n1/n2
    print(sum)


except ZeroDivisionError as e:
    print(e)
    print("enter denominator")
else:
    print()
finally:
    print("anything work here")