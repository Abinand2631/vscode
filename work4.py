#Reverse and eliminate duplicates
a="Hello world from python"[::-1]
b=list(dict.fromkeys(a))
c=len(b)
print("List is: ",b,"\nTotal lenth is: ",c)