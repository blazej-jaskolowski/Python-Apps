from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
delta = date2 - date1
print(f"{delta.days} days")
