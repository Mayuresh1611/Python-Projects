import smtplib

my_email = 'chamangotta007@gmail.com'
my_password = 'satam@1611'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email , password=my_password )
    connection.sendmail(
        from_addr=my_email,
        to_addrs= 'mayurus1611@gmail.com',
        msg= 'subject:Hello!\n\nHow are You?')
