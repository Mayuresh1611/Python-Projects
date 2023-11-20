import datetime as dt

while True:
    now = dt.datetime.now()
    given = dt.datetime(year=2021 , month=11 , day=20 , hour=23 , minute=21)
    print(now)
    if (now.month ,now.day , now.hour , now.minute ) == (given.month , given.day , given.hour , given.minute):
        print('NOW')
        break
