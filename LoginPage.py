from BasePage import *
from  time import sleep
from selenium.webdriver.common.by import By

class LoginPage(Page):
    '''首页登录页面'''

    #定位器
    username_loc = (By.ID, 'loginName')
    password_loc = (By.ID, 'loginPassword')
    login_loc    = (By.LINK_TEXT, '')
    submit_loc   = (By.ID, 'loginAction')
    search_loc   = (By.CLASS_NAME, '')
    keyword_loc  = (By.NAME, '')

    # 点击登录
    def type_login(self):
        self.find_element(*self.login_loc).click()

    # 查询
    def type_keyword(self,keyword):
        self.find_element(*self.keyword_loc).clear()
        self.find_element(*self.keyword_loc).send_keys(keyword)

    # 点击登录
    def type_search(self):
        self.find_element(*self.search_loc).click()

    #用户名输入框元素
    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    #密码输入框元素
    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    #登录按钮元素
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

#登录功能模块封装
def test_user_login(driver, username, password):
    '''测试用户名密码是否可以登录'''
    login_page = LoginPage(driver)
    # login_page.open()

    # login_page.type_keyword(keyword)
    # login_page.type_search()
    # login_page.type_login()
    # login_page.type_zmlogin()
    # sleep(4)
    login_page.type_username(username)
    login_page.type_password(password)
    sleep(4)
    login_page.type_submit()
    sleep(5)