import smtplib
import datetime as dt

def sendmail():

    with smtplib.SMTP(host='smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='chamangotta007@gmail.com' , password='satam@1611')
        connection.sendmail(
            from_addr='chamangotta007@gmail.com',
            to_addrs='mayurus1611@gmail.com',
            msg='subject:wake Up!!!\n\nThis is time to not to stop '
        )

while True:
    weekday = (dt.datetime.now()).weekday()
    print(weekday)
    if weekday == 5:
        sendmail()
        print('email sent')
        break
