def finals():
  a=1
  while a>0:
    x=input("enter the user name:")
    y=input("enter the password:")
    if(x=="g" and y=="g"):
      import booked
      booked.booking
      import last
      last.one()
    else:
      print("please enter the correct password or user name:")
      continue
    a=2
    break

    
