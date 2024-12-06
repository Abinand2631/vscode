"""fruits=["apple","banana","grapes","orange"]
result=[fruit for fruit in fruits if 'n' in fruit]
print(result)"""


# list=[1,2,3,5]
# n=2
# output=[i*n for i in list ]
# print(output)

keys=['a','b','c','d']
values=[1,2,3,4]
a=zip(keys,values)
print()
dict_values=={k:v for (k,v) in zip(keys,values)}
print(dict_values)