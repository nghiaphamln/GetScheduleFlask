import requests
from bs4 import BeautifulSoup

url = 'https://dkmh.tdmu.edu.vn/'

# Get Captcha
dataHtml = requests.get(url)
data = BeautifulSoup(dataHtml.content,'html.parser')
captcha = data.find('span', id='ctl00_ContentPlaceHolder1_ctl00_lblCapcha').text


#Bypass Captcha
values = {
    'ctl00$ContentPlaceHolder1$ctl00$txtCaptcha': 'MFJ41',
    'ctl00$ContentPlaceHolder1$ctl00$btnXacNhan': 'Vào website',
    '__VIEWSTATEGENERATOR': 'CA0B0334'
}
urlPost = 'https://dkmh.tdmu.edu.vn'
r = requests.post(urlPost, data=values)
dataCaptcha = BeautifulSoup(r.content,'html.parser')
print(dataCaptcha)