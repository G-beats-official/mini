def advance():
  print("for advance booking choose a date")

  import calendar
   
  yy=int(input("enter the year:"))
  mm =int(input("enter the month:"))
   

  print(calendar.month(yy, mm))

  import datetime 
  date=str(input('Enter the date(for example:09 02 2019):'))
  day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
  day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
  z=(day_name[day])
  print(z)
  if(z=='Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday'):
    import routes
    routes.fun()
advance()
