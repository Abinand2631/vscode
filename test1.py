a=int(input("Enter Operation : "))
if a>=5:
   exit
else:
   b=int(input("Enter 1st number : "))
   c=int(input("Enter 2nd number : "))
   if a==1:
      sum=b+c
      print(sum)
   elif a==2:
      sub=b-c
      print(sub)
   elif a==3:
      mul=b*c
      print(mul)
   elif a==4:
      if c==0:
         print("Division by zero not possible")
      else:
         div=b/c
         print(div)
