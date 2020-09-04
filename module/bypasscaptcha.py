import requests
from bs4 import BeautifulSoup
import re


# First Solve
url = 'https://dkmh.tdmu.edu.vn/'
html = requests.get(url)
cookies = html.cookies
soup = BeautifulSoup(html.content,'html.parser')


# Get Captcha
captcha = soup.find('span', id='ctl00_ContentPlaceHolder1_ctl00_lblCapcha').text


# Get __VIEWSTATE
viewstate = soup.find('input', id='__VIEWSTATE')
viewstate = re.search(" +value=\"(.*?)\"", str(viewstate))
viewstate = viewstate.group(1)


# Get __VIEWSTATEGENERATOR
viewstategenerator = soup.find('input', id='__VIEWSTATEGENERATOR')
viewstategenerator = re.search(" +value=\"(.*?)\"", str(viewstategenerator))
viewstategenerator = viewstategenerator.group(1)


# Bypass Captcha
values = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'ctl00$ContentPlaceHolder1$ctl00$txtCaptcha': captcha,
    'ctl00$ContentPlaceHolder1$ctl00$btnXacNhan': 'Vào website'
}


# Bypass Captcha Function
def GetCookies():
    requests.post(url, data = values, cookies = cookies)
    return cookies