#coding:utf8
import sys

from selenium import webdriver
import time, re, random

from LoginPage import test_user_login

'''
url1 登录的路径
url2 抓取页面的路径
page_num 要抓取的页面数量
save_path 保存文件的路径
'''
def crawler(url1, url2, page_num, save_path):
    browser = webdriver.Chrome()
    ###### for linux ######
    # browser = webdriver.Chrome("./chromedriver")

    browser.get(url1)
    #人工登录阶段
    time.sleep(5)
    sumpage = page_num
    fw = open(save_path, 'a', encoding='utf-8')
    browser.get(r'http://weibo.cn/breakingnews?page=2')
    time.sleep(5)

    # 输入微博用户名和密码
    test_user_login(browser, "username", "password")

    for page in range(1,sumpage+1):
        browser.get(url2+str(page))
        html = browser.page_source
        print ('PageNumber: '+ str(page))
        # pattern = re.compile('(【.*?)<a')
        # result = pattern.findall(html)
        # temp = ''
        # for r in result:
        #     if(len(r)<180):
        #         # print r
        #         continue
        #     temp += r+'\n'
        # fw.write(temp)
        print (html)
        fw.write(html+'\n')
        # 防反爬策略
        time.sleep(1+random.randint(1,9))

    print ('end')



crawler('http://weibo.com/', 'http://weibo.cn/breakingnews?page=', 12147, "result1-12147.txt")

# crawler('http://news.qq.com/', 'http://news.qq.com/20180422/20180422', 12147, "result1-12147.txt")

