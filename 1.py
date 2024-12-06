a=int(input("Enter Operation : "))
b=int(input("Enter 1st number : "))
c=int(input("Enter 2nd number : "))
if a==1:
   sum=a+b
   print(sum)
elif a==2:
   sub=a-b
   print(sub)
elif a==3:
   mul=a*b
   print(mul)
elif a==4:
   if c==0:
      print("Division by zero not possible")
   else:
      div=a/b
      print(div)
else:
   exit


