#method 1
import datetime

if 4%int(datetime.date.today().year) == 0:
    print(f"This is year {datetime.date.today().year}, and it's a leap year.")
else:
    print(f"This is year {datetime.date.today().year}, and it's not a leap year.")
