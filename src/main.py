import datetime

plate='pbx1024'
# day/month/year/
date='1/8/2023'
# 24:00 hours format
time= datetime.time(11, 30)
print(time)


def pico_placa_detector (placa,date,time):
    
    print()
    
def day_date(date):
  # String to datetime
  date_datetime = datetime.datetime.strptime(date, '%d/%m/%Y')

  # Obtain the day of the week number (0=Monday, 6=Sunday)
  number_day_week = date_datetime.weekday()

  days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  day = days_week[number_day_week]

  return day

print( day_date(date) )
