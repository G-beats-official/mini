def booking():
    a=1
    while a>0:
      print("press 1 to instant booking")
      print("press 2 to advance booking")
      x=int(input("enter the number:"))
      if(x==1):
        from datetime import date

        today = date.today()
        print("HAVE A NICE DAY", today)
        import instant
        instant.instant()
      if(x==2):
        import date
        date.advance()
      if(x!=1 and x!=2):
          print("try again")
          continue
      a=2
      break

booking()

