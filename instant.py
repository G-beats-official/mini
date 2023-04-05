def instant():

  a=1
  while a>0:
    print("press 1 to start booking")
    x=int(input("enter the number:"))
    if(x==1):
        import routes
        routes.fun()
        break
    if(x!=1):
        print("try again")
        continue
    a=2
    break


