from smtplib  import *      
import datetime as dt      
from pandas import *      

my_email = 'chamangotta007@gmail.com'      
my_pass = 'satam@1611'      
to_email = 'mayurus1611@gmail.com'      

data =  read_csv('important_dates.csv')      
dates_list = data.to_dict(orient='records')      

def send_mail(date ,day, festival):      
    with SMTP(host='smtp.gmail.com') as connection:      
        connection.starttls()      
        connection.login(user=my_email , password=my_pass)      
        connection.sendmail(from_addr= my_email ,      
         to_addrs= to_email ,       
         msg=f"subject: Today's date {day} - {date}\n\nToday is {festival}")      

while True:      
    today = dt.datetime.now()      
    for day in dates_list:      
        if (today.day , today.month) == (day['date'] , day['month']+1):      
            send_mail(day['date'] , day['day'] , day['name'])      
            