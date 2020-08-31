year = 2020

if year % 400 == 0 or (year % 4 == 0 and year % 100):
    print(True)
else:
    print(False)