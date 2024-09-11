import datetime


def day_date(date):
  # String to datetime
  date_datetime = datetime.datetime.strptime(date, '%d/%m/%Y')

  # Obtain the day of the week number (0=Monday, 6=Sunday)
  number_day_week = date_datetime.weekday()

  days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  day = days_week[number_day_week]

  return day


def is_vehicle_allowed(day_week, plate):
  if day_week in ("Sunday", "Saturday"):
    return True

  last_digit = plate[-1]
  restricted_digits = {
    "Monday": ("1", "2"),
    "Tuesday": ("3", "4"),
    "Wednesday": ("5", "6"),
    "Thursday": ("7", "8"),
    "Friday": ("9", "0")
  }

  if last_digit in restricted_digits.get(day_week, ()):
    return False

  return True



def pico_placa_detector (plate,date,time):
    morning_pico_placa_start=datetime.time(7,0)
    morning_pico_placa_end=datetime.time(9,30)

    afternoon_pico_placa_start=datetime.time(16,0)
    afternoon_pico_placa_end=datetime.time(19,30)
    
    day_week=day_date(date)
    if not (morning_pico_placa_start <= time <= morning_pico_placa_end or  afternoon_pico_placa_start <= time <= afternoon_pico_placa_end):
        return True
    else:
        return is_vehicle_allowed(day_week,plate)


""""
plate='xyz5678'
# day/month/year/
date='10/9/2024'
# 24:00 hours format
time= datetime.time(8, 30)
print(time)
print(plate[-1])



print( day_date(date) )

print(pico_placa_detector(plate,date,time))


"""


def enter_data():

    plate = input("Enter a vehicle plate (example: ABC1234): ")
    date_input = input("Enter a date (format DD/MM/YYYY): ")
    
    try:
        date = datetime.datetime.strptime(date_input, "%d/%m/%Y").strftime('%d/%m/%Y')
    except ValueError:
        print("Error: Invalid date format. Try again.")
        return
    
    time_input = input("Enter the time (format HH:MM, 24 hours): ")
    
    try:
        time = datetime.datetime.strptime(time_input, "%H:%M").time()
    except ValueError:
        print("Error: Invalid time format. Try again.")
        return
    
    if pico_placa_detector(plate, date, time):
        print("The car is allowed to circulate")
    else:
        print("The car ISN'T allowed to circulate")


if __name__ == "__main__":
    while True:
        enter_data()
        
        another = input("Do you want to check another vehicle plate? (y/n): ").lower()
        if another != 'y':
            print("Good bye!")
            break