import requests
import smtplib

'''52.876,-14.919,6'''
'''
'lat':18.520430,
'lon':73.856743,
'''

My_email = 'chamangotta007@gmail.com'
My_pass = 'gotta@007'
To_email = 'mayurus1611@gmail.com'

API_Key = '6b64220eb23eca962dd7857fce52bd94'
URL = 'https://api.openweathermap.org/data/2.5/onecall?'
API_Params = {
    'lat':52.876,
    'lon':-14.919,
    'appid':'6b64220eb23eca962dd7857fce52bd94',
    'exclude':'current,minutely,daily,alerts'
}

def send_mail():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=My_email , password=My_pass)
        connection.sendmail(
            from_addr= My_email,
            to_addrs= To_email,
            msg= 'subject: Good Morning, Today\'s Weather Forecast\n\nBring Umbrella bOYYYY'
            )

response = requests.get(URL , params=API_Params )
report = response.json()

weather_data = report['hourly'][:12]

for hour_data in weather_data:
    id = (hour_data['weather'][0]['id'])
    if id < 800:
        print('Bring Umbrella')
        send_mail()
        break
        