import pytest
from selenium import webdriver
from time import sleep
from pages.register_page import RegisterPage
from pages.users_login_page import UsersLoginPage
from pages.users_feedbackiframe_page import UsersFeedbackiframePage
from pages.users_userinfo_page import UsersUserinfoPage
from common.connect_mysql import DbConnect,dbinfo
import platform
from selenium.webdriver.chrome.options import Options

'''
@pytest.fixture(scope='session',name='driver')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    sleep(1)
    driver.quit()
'''

# 代码兼容windows和linux系统运行
@pytest.fixture(scope='session', name='driver')
def browser():
    '''定义一个全局driver'''
    if platform.system() == 'Windows':
        # windows系统
        _driver = webdriver.Chrome()
        _driver.maximize_window()
    else:
        #linux系统
        chrome_options = Options()
        chrome_options.add_argument('--windows-size=1920,1080')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--headless')

        # _driver = webdriver.Chrome()
        _driver = webdriver.Chrome(chrome_options=chrome_options)

    yield _driver
    #退出浏览器
    _driver.quit()

@pytest.fixture(scope='session')
def base_url():
    url = 'http://49.235.92.12:8200'
    return url



@pytest.fixture(scope='session')
def registerPage(driver,base_url):
    # 注册页面实例化
    register = RegisterPage(driver, base_url)
    return register


@pytest.fixture(scope='session')
def usersLoginPage(driver,base_url):
    # 登录页面实例化
    userslogin = UsersLoginPage(driver,base_url)
    return userslogin


@pytest.fixture(scope='session')
def userfeedbackPage(driver,base_url):
    # 意见反馈页面实例化
    usersfeedback = UsersFeedbackiframePage(driver,base_url)
    return usersfeedback


@pytest.fixture(scope='session')
def login_driver(driver,usersLoginPage):
    '''用户先登录，返回driver'''
    usersLoginPage.open('/users/login/')
    usersLoginPage.input_login_username('1234@qq.com')
    usersLoginPage.input_login_password('123456')
    usersLoginPage.click_login_btn()
    return driver


@pytest.fixture(scope='session')
def usersUserinfoPage(login_driver,base_url):
    # 个人资料页面实例化 ，需要先进行登录
    usersUserinfo = UsersUserinfoPage(login_driver,base_url)
    return usersUserinfo


@pytest.fixture(scope='session')
def db():
    #db数据库连接实例化
    _db = DbConnect(dbinfo,'online')
    #返回db
    yield _db
    #关闭db连接
    _db.close()



#场景：解决ids参数用例标题中文Unicode编码问题，使用hooks函数
def pytest_collection_modifyitems(items):
    '''测试用例收集完成时，将收集到的items的name和nodeid的中文显示控制台'''
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")