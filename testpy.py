import shelve
import time

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#ewqeq6546565

class Test_Cookies():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        db=shelve.open("cookies")#保存cookies到数据库
        # db['cookie']=self.driver.get_cookies()
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851266845970'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324976466208'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851266845970'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4216216'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '01894273'}, {'domain': '.work.weixin.qq.com', 'expiry': 1675935110, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'TIZ-YoOSUV6iGt-XvO1N-xptCBDGUOsao62X4i62e9aRgPLc7iavJRJFVBKh4i6-6Tre0Oyb0vQ72sW6DHk25r_V0-GC4ZCgMoXDhAqpbUXpNerF_v5UNILv7QsFJhN5XHYV3UZSMwZ94mVeRZIKsx0fKnlhLtumbtXD-8QjpIbgm-2zYub2FYm-tCb3I9jjKhRYaVXwoNFJ8zr_VNV_b3YeHXEvVG7I7Bs5yWrOa7GOEcD73SYkAbp04lh6N-G6WSiZDdYwGHiQxrA1HWfKQg'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '1fnpNFn2NIXqCneCOS4l35XDdRVf8qETPYwGui2C-9wC0jbDDJ4C3ClWZhtFK8Nk'}, {'domain': '.work.weixin.qq.com', 'expiry': 1704877972, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}]
        # print(self.driver.get_cookies())
        cookies=db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(5)
