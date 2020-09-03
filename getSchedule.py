import requests
import connectDB
from bs4 import BeautifulSoup


# Get web page
# user = '1824801040118'
url = 'https://dkmh.tdmu.edu.vn/'

# Get information of student
def getInformation(user):
    dataHtml = requests.get(url + 'default.aspx?page=thoikhoabieu&sta=0&id=' + user)
    data = BeautifulSoup(dataHtml.content, "html.parser")
    information = data.find('span', id = 'ctl00_ContentPlaceHolder1_ctl00_lblContentTenSV').text
    information += data.find('span', id = 'ctl00_ContentPlaceHolder1_ctl00_lblLop').text
    information += data.find('span', id = 'ctl00_ContentPlaceHolder1_ctl00_lblContentLopSV').text
    return information



# Check MSSV
def checkMSSV(user):
    try:
        getInformation(user)
        return bool(1)
    except:
        return bool(0)




# Get Schedule
def getSchedule(user):
    fullSubjects = []
    dataHtml = requests.get(url + 'default.aspx?page=thoikhoabieu&sta=0&id=' + user)
    data = BeautifulSoup(dataHtml.content, "html.parser")
    dataSchedule = data.findAll('td', onmouseout = 'hideddrivetip()')
    for subject in dataSchedule:
        subject = subject.attrs
        subject = subject['onmouseover']
        subject = subject.replace("ddrivetip('", '')
        subject = subject.replace("')", '')
        subject = subject.split("','")
        fullSubjects.append(subject)

    # convert day to integer
    for i in fullSubjects:
        if i[3] == 'Thứ Hai':
            i[3] = 0
        elif i[3] == 'Thứ Ba':
            i[3] = 1
        elif i[3] == 'Thứ Tư':
            i[3] = 2
        elif i[3] == 'Thứ Năm':
            i[3] = 3
        elif i[3] == 'Thứ Sáu':
            i[3] = 4
        elif i[3] == 'Thứ Bảy':
            i[3] = 5
        elif i[3] == 'Chủ Nhật':
            i[3] = 6

    information = getInformation(user)
    information = information.split('-')

    message = 'Chào cậu - ' + information[0] + ' (' + information[2] + ')!\nLịch học tuần này của cậu là: '

    dayOfWeek = ['Thứ Hai', 'Thứ Ba', 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu', 'Thứ Bảy', 'Chủ Nhật']

    for i in range(0, 7):
        message_subject = ''
        for subject in fullSubjects:
            if (subject[3] == i):
                message_subject += '\n ⏰ ' + subject[1]
                message_subject += '\n   + Phòng học: ' + subject[5]
                message_subject += '\n   + Giảng viên: ' + subject[8]
                message_subject += '\n   + Bắt đầu: Tiết ' + subject[6]
                message_subject += '\n   + Kết thúc: Tiết ' + str(int(subject[6]) + int(subject[7]))
        if (message_subject != ''):
            message += '\n\n🔥 '+ dayOfWeek[i] +' 🔥'
            message += message_subject

    return message

user = '1824801030067'
fb_id = '123'

# Test Insert
if checkMSSV(user):
    try:
        connectDB.insertMSSV(fb_id, user)
        print('Done!')
    except:
        print('MSSV Existed!')
else:
    print('Can\'t find MSSV')