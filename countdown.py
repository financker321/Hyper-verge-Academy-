import datetime

def user_bday():
    print("When you where born? [DD-MM-YYYY]")
    x = (input()).split('-')
    day = int(x[0])
    month = int(x[1])
    year = int(x[2])
    birthday = datetime.date(year,month,day)
    return birthday

def cal_dates(bday_date, now):
    this_year = datetime.datetime(now.year, bday_date.month, bday_date.day)
    date = this_year - now
    hours = date.total_seconds()//3600
    minutes = (date.total_seconds()%3600)//60
    seconds = (date.total_seconds()%3600)%60
    return hours,minutes,seconds

bornday = user_bday()
today = datetime.datetime.today()
countdown = cal_dates(bornday, today)
print("Your birthday is in {} hours".format(int(countdown[0])),"{} minutes".format(int(countdown[1])),"{} seconds".format(int(countdown[2])))
