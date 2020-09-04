import requests
from bs4 import BeautifulSoup
import re

#Soup
url = 'https://dkmh.tdmu.edu.vn/'
dataHtml = requests.get(url)
cookies = dataHtml.cookies
data = BeautifulSoup(dataHtml.content,'html.parser')

# Get Captcha
captcha = data.find('span', id='ctl00_ContentPlaceHolder1_ctl00_lblCapcha').text

# Get __VIEWSTATE
viewstate = data.find('input', id='__VIEWSTATE')
viewstate = re.search(" +value=\"(.*?)\"", str(viewstate))
viewstate = viewstate.group(1)

# Get __VIEWSTATEGENERATOR
viewstategenerator = data.find('input', id='__VIEWSTATEGENERATOR')
viewstategenerator = re.search(" +value=\"(.*?)\"", str(viewstategenerator))
viewstategenerator = viewstategenerator.group(1)

# Bypass Captcha
values = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'ctl00$ContentPlaceHolder1$ctl00$txtCaptcha': captcha,
    'ctl00$ContentPlaceHolder1$ctl00$btnXacNhan': 'Vào website'
}
#cookies = dict(cookies_are='working')
requests.post(url, data = values, cookies = cookies)


# Get information of student
user = '1824801040118'

dataHtml = requests.get(url + 'default.aspx?page=thoikhoabieu&sta=0&id=' + user, cookies = cookies)
data = BeautifulSoup(dataHtml.content, "html.parser")
information = data.find('span', id = 'ctl00_ContentPlaceHolder1_ctl00_lblContentTenSV').text
information += data.find('span', id = 'ctl00_ContentPlaceHolder1_ctl00_lblLop').text
information += data.find('span', id = 'ctl00_ContentPlaceHolder1_ctl00_lblContentLopSV').text
print(information)
