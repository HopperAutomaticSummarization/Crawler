from  time import sleep

class Page():
    '''页面基础类'''

    #初始化
    def __init__(self, dirver):
        self.base_url = dirver.current_url
        self.driver = dirver
        # self.timeout = 10

    #打开不同的子页面
    def _open(self):
        url_ = self.base_url
        print(self.driver)
        # self.driver.maximize_window()
        self.driver.get(self.base_url)
        # sleep(2)
        # print(self.driver.current_url)
        assert self.driver.current_url == url_, 'Did ont land on %s' % url_

    def open(self):
        self._open()

    #元素定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)