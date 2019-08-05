#coding=utf-8
import time
from selenium import webdriver
# 设置请求头部信息
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
               'Accept': '*/*',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip',
               'Connection': 'close',
               'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
               }
driver = webdriver.Firefox()
driver.get(r'http://admin.playapper.com:8080/jinrizhuan/sys/index')


def login():
    driver.find_element_by_xpath('//*[@id="user-name"]').send_keys('glt')
    driver.find_element_by_xpath('//*[@id="user-pass"]').send_keys('123456')
    login = driver.find_element_by_xpath('//*[@id="login"]')
    login.click()


def addJiek():
    # driver.find_element_by_xpath('//*[@id="menu"]/div[6]/div[1]/div[1]').click()
    # driver.find_element_by_xpath('//*[@id="161110"]').click()
    # driver.find_element_by_link_text('接口添加').click()
    driver.get('http://admin.playapper.com:8080/jinrizhuan/abutment/add')


def addquery(check):
    # 排重接口选择  是
    driver.find_element_by_xpath('//*[@id="panel2"]/div[1]/div[3]/input').click()
    # 排重地址
    driver.find_element_by_xpath('//*[@id="panel2"]/div[3]/div[4]/span/input[1]').send_keys('http://api.wsaso.com:8080/check/channel_idfa_query')
    for num in range(1,10):
        driver.find_element_by_xpath('//*[@id="checkDIV"]/span/span[2]').click()
    driver.find_element_by_xpath('//*[@id="checkParDiv0"]/div[2]/span/input[1]').send_keys('adid')
    driver.find_element_by_xpath('//*[@id="checkParDiv0"]/div[4]/span/input[1]').send_keys('adid')

    driver.find_element_by_xpath('//*[@id="checkParDiv1"]/div[2]/span/input[1]').send_keys('idfas')
    driver.find_element_by_xpath('//*[@id="checkParDiv1"]/div[4]/span/input[1]').send_keys('idfa')

    driver.find_element_by_xpath('//*[@id="checkParDiv2"]/div[2]/span/input[1]').send_keys('channel')
    driver.find_element_by_xpath('//*[@id="checkParDiv2"]/div[4]/span/input[1]').send_keys('jinrizhuan')

    driver.find_element_by_xpath('//*[@id="checkParDiv3"]/div[2]/span/input[1]').send_keys('check')
    driver.find_element_by_xpath('//*[@id="checkParDiv3"]/div[4]/span/input[1]').send_keys(check)

    driver.find_element_by_xpath('//*[@id="checkParDiv4"]/div[2]/span/input[1]').send_keys('ip')
    driver.find_element_by_xpath('//*[@id="checkParDiv4"]/div[4]/span/input[1]').send_keys('ip')

    driver.find_element_by_xpath('//*[@id="checkParDiv5"]/div[2]/span/input[1]').send_keys('os')
    driver.find_element_by_xpath('//*[@id="checkParDiv5"]/div[4]/span/input[1]').send_keys('os')

    driver.find_element_by_xpath('//*[@id="checkParDiv6"]/div[2]/span/input[1]').send_keys('devType')
    driver.find_element_by_xpath('//*[@id="checkParDiv6"]/div[4]/span/input[1]').send_keys('devType')

    driver.find_element_by_xpath('//*[@id="checkParDiv7"]/div[2]/span/input[1]').send_keys('udid')
    driver.find_element_by_xpath('//*[@id="checkParDiv7"]/div[4]/span/input[1]').send_keys('udid')

    driver.find_element_by_xpath('//*[@id="checkParDiv8"]/div[2]/span/input[1]').send_keys('keyword')
    driver.find_element_by_xpath('//*[@id="checkParDiv8"]/div[4]/span/input[1]').send_keys('keyword')

    driver.find_element_by_xpath('//*[@id="checkParDiv9"]/div[2]/span/input[1]').send_keys('type_jinrizhuan')
    driver.find_element_by_xpath('//*[@id="checkParDiv9"]/div[4]/span/input[1]').send_keys('qianke')

    driver.find_element_by_xpath('//*[@id="panel2"]/div[5]/div[6]/span/input[1]').send_keys(1)
    driver.find_element_by_xpath('//*[@id="panel2"]/div[5]/div[8]/span/input[1]').send_keys(0)


def addClick(isCallback):
    # 点击接口 选择是
    driver.find_element_by_xpath('//*[@id="panel3"]/div[1]/div[3]/input').click()
    driver.find_element_by_xpath('//*[@id="panel3"]/div[3]/div[4]/span/input[1]').send_keys('http://api.wsaso.com:8080/click/channel_idfa_click')
    # isCallback  0 回调 1没有回调
    if isCallback == 0:
        driver.find_element_by_xpath('//*[@id="panel3"]/div[2]/div[3]/input').click()
    for num in range(1, 10):
        driver.find_element_by_xpath('//*[@id="clickDIV"]/span/span[2]').click()

    driver.find_element_by_xpath('//*[@id="clickParDiv0"]/div[2]/span/input[1]').send_keys('adid')
    driver.find_element_by_xpath('//*[@id="clickParDiv0"]/div[4]/span/input[1]').send_keys('')

    driver.find_element_by_xpath('//*[@id="clickParDiv10"]/div[2]/span/input[1]').send_keys('idfa')
    driver.find_element_by_xpath('//*[@id="clickParDiv10"]/div[4]/span/input[1]').send_keys('idfa')

    driver.find_element_by_xpath('//*[@id="clickParDiv11"]/div[2]/span/input[1]').send_keys('channel')
    driver.find_element_by_xpath('//*[@id="clickParDiv11"]/div[4]/span/input[1]').send_keys('jinrizhuan')

    driver.find_element_by_xpath('//*[@id="clickParDiv12"]/div[2]/span/input[1]').send_keys('callbackurl')
    driver.find_element_by_xpath('//*[@id="clickParDiv12"]/div[4]/span/input[1]').send_keys('callback')

    driver.find_element_by_xpath('//*[@id="clickParDiv13"]/div[2]/span/input[1]').send_keys('keyword')
    driver.find_element_by_xpath('//*[@id="clickParDiv13"]/div[4]/span/input[1]').send_keys('keyword')

    driver.find_element_by_xpath('//*[@id="clickParDiv14"]/div[2]/span/input[1]').send_keys('ip')
    driver.find_element_by_xpath('//*[@id="clickParDiv14"]/div[4]/span/input[1]').send_keys('ip')

    driver.find_element_by_xpath('//*[@id="clickParDiv15"]/div[2]/span/input[1]').send_keys('mac')
    driver.find_element_by_xpath('//*[@id="clickParDiv15"]/div[4]/span/input[1]').send_keys('020000000000')

    driver.find_element_by_xpath('//*[@id="clickParDiv16"]/div[2]/span/input[1]').send_keys('os')
    driver.find_element_by_xpath('//*[@id="clickParDiv16"]/div[4]/span/input[1]').send_keys('os')

    driver.find_element_by_xpath('//*[@id="clickParDiv17"]/div[2]/span/input[1]').send_keys('devType')
    driver.find_element_by_xpath('//*[@id="clickParDiv17"]/div[4]/span/input[1]').send_keys('devType')

    driver.find_element_by_xpath('//*[@id="clickParDiv18"]/div[2]/span/input[1]').send_keys('udid')
    driver.find_element_by_xpath('//*[@id="clickParDiv18"]/div[4]/span/input[1]').send_keys('udid')

    driver.find_element_by_xpath('//*[@id="panel3"]/div[5]/div[4]/span/input[1]').send_keys('code')
    driver.find_element_by_xpath('//*[@id="panel3"]/div[5]/div[6]/span/input[1]').send_keys(0)
    driver.find_element_by_xpath('//*[@id="panel3"]/div[5]/div[8]/span/input[1]').send_keys(1)


def addReport(type):
    # type 0本地上报  1上报
    # 上报接口 选择是
    driver.find_element_by_xpath('//*[@id="panel4"]/div[1]/div[3]/input').click()
    driver.find_element_by_xpath('//*[@id="panel4"]/div[2]/div[4]/span/input[1]').send_keys('http://api.wsaso.com:8080/report/channel_idfa_report')

    for num in range(1, 9):
        driver.find_element_by_xpath('//*[@id="reportDIV"]/span/span[2]').click()

    driver.find_element_by_xpath('//*[@id="reportParDiv0"]/div[2]/span/input[1]').send_keys('adid')
    driver.find_element_by_xpath('//*[@id="reportParDiv0"]/div[4]/span/input[1]').send_keys('')

    driver.find_element_by_xpath('//*[@id="reportParDiv19"]/div[2]/span/input[1]').send_keys('idfa')
    driver.find_element_by_xpath('//*[@id="reportParDiv19"]/div[4]/span/input[1]').send_keys('idfa')

    driver.find_element_by_xpath('//*[@id="reportParDiv20"]/div[2]/span/input[1]').send_keys('channel')
    driver.find_element_by_xpath('//*[@id="reportParDiv20"]/div[4]/span/input[1]').send_keys('jinrizhuan')

    driver.find_element_by_xpath('//*[@id="reportParDiv21"]/div[2]/span/input[1]').send_keys('keyword')
    driver.find_element_by_xpath('//*[@id="reportParDiv21"]/div[4]/span/input[1]').send_keys('keyword')

    driver.find_element_by_xpath('//*[@id="reportParDiv22"]/div[2]/span/input[1]').send_keys('type')
    driver.find_element_by_xpath('//*[@id="reportParDiv22"]/div[4]/span/input[1]').send_keys(type)

    driver.find_element_by_xpath('//*[@id="reportParDiv23"]/div[2]/span/input[1]').send_keys('ip')
    driver.find_element_by_xpath('//*[@id="reportParDiv23"]/div[4]/span/input[1]').send_keys('ip')

    driver.find_element_by_xpath('//*[@id="reportParDiv24"]/div[2]/span/input[1]').send_keys('os')
    driver.find_element_by_xpath('//*[@id="reportParDiv24"]/div[4]/span/input[1]').send_keys('os')

    driver.find_element_by_xpath('//*[@id="reportParDiv25"]/div[2]/span/input[1]').send_keys('devType')
    driver.find_element_by_xpath('//*[@id="reportParDiv25"]/div[4]/span/input[1]').send_keys('devType')

    driver.find_element_by_xpath('//*[@id="reportParDiv26"]/div[2]/span/input[1]').send_keys('udid')
    driver.find_element_by_xpath('//*[@id="reportParDiv26"]/div[4]/span/input[1]').send_keys('udid')

    driver.find_element_by_xpath('//*[@id="panel4"]/div[4]/div[4]/span/input[1]').send_keys('code')
    driver.find_element_by_xpath('//*[@id="panel4"]/div[4]/div[6]/span/input[1]').send_keys(0)
    driver.find_element_by_xpath('//*[@id="panel4"]/div[4]/div[8]/span/input[1]').send_keys(1)


def findAdid(id):
    # driver.get('http://admin.playapper.com:8080/jinrizhuan/abutment/list')
    # driver.find_element_by_xpath('//*[@id="leftdiv"]/span[4]/input[1]').send_keys(adid)
    # driver.find_element_by_xpath('//*[@id="searchabutment"]/span').click()
    edit_url = 'http://admin.playapper.com:8080/jinrizhuan/abutment/'+id+'/toupdate'
    driver.get(edit_url)
    # driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[9]/div/a[2]').click()


def addCQClick(isCallback):
    # 点击接口 选择是
    driver.find_element_by_xpath('//*[@id="panel3"]/div[1]/div[3]/input').click()
    driver.find_element_by_xpath('//*[@id="panel3"]/div[3]/div[4]/span/input[1]').send_keys('http://dc.chuangqish.cn/connect/308/report')
    # isCallback  0 回调 1没有回调
    if isCallback == 0:
        driver.find_element_by_xpath('//*[@id="panel3"]/div[2]/div[3]/input').click()
    for num in range(1, 10):
        driver.find_element_by_xpath('//*[@id="clickDIV"]/span/span[2]').click()

    driver.find_element_by_xpath('//*[@id="panel2"]/div[3]/div[2]/span/input[1]').send_keys('get')

    driver.find_element_by_xpath('//*[@id="clickParDiv0"]/div[2]/span/input[1]').send_keys('appid')
    driver.find_element_by_xpath('//*[@id="clickParDiv0"]/div[4]/span/input[1]').send_keys('')

    driver.find_element_by_xpath('//*[@id="clickParDiv14"]/div[2]/span/input[1]').send_keys('idfa')
    driver.find_element_by_xpath('//*[@id="clickParDiv14"]/div[4]/span/input[1]').send_keys('idfa')

    driver.find_element_by_xpath('//*[@id="clickParDiv15"]/div[2]/span/input[1]').send_keys('ip')
    driver.find_element_by_xpath('//*[@id="clickParDiv15"]/div[4]/span/input[1]').send_keys('ip')

    driver.find_element_by_xpath('//*[@id="clickParDiv16"]/div[2]/span/input[1]').send_keys('keyword')
    driver.find_element_by_xpath('//*[@id="clickParDiv16"]/div[4]/span/input[1]').send_keys('keyword')

    driver.find_element_by_xpath('//*[@id="clickParDiv17"]/div[2]/span/input[1]').send_keys('model')
    driver.find_element_by_xpath('//*[@id="clickParDiv17"]/div[4]/span/input[1]').send_keys('devType')

    driver.find_element_by_xpath('//*[@id="clickParDiv18"]/div[2]/span/input[1]').send_keys('os')
    driver.find_element_by_xpath('//*[@id="clickParDiv18"]/div[4]/span/input[1]').send_keys('os')

    driver.find_element_by_xpath('//*[@id="clickParDiv19"]/div[2]/span/input[1]').send_keys('udid')
    driver.find_element_by_xpath('//*[@id="clickParDiv19"]/div[4]/span/input[1]').send_keys('udid')

    driver.find_element_by_xpath('//*[@id="panel3"]/div[5]/div[4]/span/input[1]').send_keys('success')
    driver.find_element_by_xpath('//*[@id="panel3"]/div[5]/div[6]/span/input[1]').send_keys('true')
    driver.find_element_by_xpath('//*[@id="panel3"]/div[5]/div[8]/span/input[1]').send_keys('false')


def quDao():
    driver.get('http://admin.playapper.com:8080/jinrizhuan/channel_task/getTodayTask?appname=&startTime=&endTime=&upOrDown=&page=1&rows=20')


if __name__ == '__main__':
    # 钱课下放今日赚，在今日赚上配
    login()
    quDao()
    #findAdid('3023')
    #addCQClick(1)

    # check  0本地排重  1排重
    # addquery(check=1)
    # isCallback  0 回调 1没有回调
    # addClick(isCallback=1)
    # type 0本地上报  1上报
    # addReport(type=1)






