import requests

url_passport = 'https://passport.yandex.ru/auth/'

data = {'login':'tzapisimbir',
         'passwd':'SimbirS0ft'
         }

def loging():
    headers = {'user-agent': 'Mozilla/5.0'}
    session = requests.Session()
    session.post(url_passport, headers=headers, data=data)
