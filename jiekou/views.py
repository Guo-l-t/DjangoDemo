from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import Jiekou
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from selenium import webdriver
from django.template import RequestContext
import os


def query_to_dic(query):
    dic = model_to_dict(query)


def index(request):
    bir = Jiekou.objects.all()
    return render(request, 'jiekou/index.html', {'bir': bir, 'download': 'download'})


def download(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
    print(base_dir)

    print('-------')
    print('-------')
    print('-------')
    print('-------')
    return render(request, 'jiekou/index.html', {'flag': '1'})

def upload(request):

    if request.method == 'POST':
        uploadFile = request.FILES.get('filename')
        if not uploadFile:
            return render(request, 'upload.html', {'msg': '没有选择文件！！！'})
        if not uploadFile.name.endswith('.csv'):
            return render(request, 'upload.html', {'msg': '必须选择csv文件！！！'})
        destination = open(os.path.join("D:\\git_project\\DjangoDemo\\resource\\jiekou\\upload", uploadFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in uploadFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
    print(uploadFile)
    # pass
    return render(request, 'jiekou/index.html', {'flag': '1'})


def add_jrz(request):
    # 排重  0 本地排重   1 排重   2不排重
    query = request.GET['query']
    # 排重地址
    queryurl = request.GET['queryurl']
    # 排重  0 点击
    click = request.GET['click']
    # 点击地址
    clickurl = request.GET['clickurl']
    # 回调 0 回调   1不回调
    iscallback = request.GET['callback']
    # 上报  0 本地上报   1 上报   2 不上报
    report = request.GET['report']
    # 上报地址
    reporturl = request.GET['reporturl']

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
               'Accept': '*/*',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'gzip',
               'Connection': 'close',
               'Referer': 'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
               }
    driver = webdriver.Firefox()
    driver.get(r'http://admin.playapper.com:8080/jinrizhuan/sys/index')

    login(driver)
    addJiek(driver)
    if query != '2':
        addquery(driver, query)
    if click != '1':
        addClick(driver, iscallback)
    if report != '2':
        addReport(driver, report)

    return render(request, 'jiekou/index.html')


def login(driver):
    driver.find_element_by_xpath('//*[@id="user-name"]').send_keys('glt')
    driver.find_element_by_xpath('//*[@id="user-pass"]').send_keys('123456')
    login = driver.find_element_by_xpath('//*[@id="login"]')
    login.click()


def addJiek(driver):
    # driver.find_element_by_xpath('//*[@id="menu"]/div[6]/div[1]/div[1]').click()
    # driver.find_element_by_xpath('//*[@id="161110"]').click()
    # driver.find_element_by_link_text('接口添加').click()
    return driver.get('http://admin.playapper.com:8080/jinrizhuan/abutment/add')


def addquery(driver, check):
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


def addClick(driver, isCallback):
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


def addReport(driver, type):
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

