a=input("Enter Username: ")
b=a.isalnum()
if b==True:
   if 6<len(a)<15:
      print("The username is valid")
   else:
      print("The username is invalid")
else:
   print("The username is inavlid")
