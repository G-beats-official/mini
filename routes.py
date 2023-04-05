def fun():
  print("To view the route map press 1")
  z=int(input("enter the number:"))
  if(z==1):
    print("""          0 for thirumangalam,
           1 for anna nagar tower,
           2 for anna nagar East",
           3 for Shenoy Nagar,
           4 for pachiyappas college,
           5 for Egmore,
           6 for Central""")
  list=["thirumangalam","anna nagar tower","anna nagar East","shenoy Nagar","Pachiyappas college","Egmore","Central"]
  x=int(input("enter the starting point:"))
  y=int(input("enter the ending point:"))
  if(x==0,1,2,3,4,5,6):
     print("your starting point is:",list[x])
  if(y==0,1,2,3,4,5,6):
    print("your destignation is:",list[y])
  if(x==y):
    print("please enter the correct option")
  if(x==0 and (y==1 or y==2 or y==3)):
    print("the price of the ticket is $10")
    exit()
  if(x==0 and (y==4 or y==5 or y==6)):
    print("the price of the ticket is $20")
    exit()
  if(x==1 and (y==0 or y==1 or y==2 or y==3)):
    print("the price of the ticket is $10")
    exit()
  if(x==1 and(y==4 or y==5 or y==6)):
    print("the price of the ticket is $20")
    exit()
  if(x==2 and (y==0 or y==1 or y==2 or y==3 or y==4)):
    print("the price of the ticket is $10")
    exit()
  if(x==2 and (y==5 or y==6 or y==7)):
   print("the price of the ticket is $20")
   exit()
  if(x==3 and (y==0 or y==1 or y==2 or y==4)):
   print("the price of the ticket is $10")
   exit()
  if(x==3 and (y==5 or y==6 or y==7)):
   print("the price of the ticket is $20")
   exit()
  if(x==4 and (y==0 or y==1 or y==2 or y==3)):
   print("the price of the ticket is $10")
   exit()
  if(x==4 and(y==4 or y==5 or y==6 or y==7)):
   print("the price of the ticket is $20")
   exit()
  if(x==5 and(y==1 or y==2 or y==3 or y==4)):
   print("the price of the ticket is $10")
   exit()
  if(x==5 and(y==5 or y==6 or y==7)):
   print("the price of the ticket is $20")
   exit()
  if(x==6 and(y==1 or y==2 or y==3 or y==4)):
   print("the price of the ticket is $20")
   exit()
  if(x==6 and(y==5 or y==6 or y==7)):
   print("the price of the ticket is $10")
   exit()
  if(x==7 and (y==1 or y==2 or y==3 or y==4)):
   print("the price of the ticket is $20")
   exit()
  if(x==7 and (y==5 or y==6)):
   print("the price of the ticket is $10")
   exit()
  print("thank you visit again")

