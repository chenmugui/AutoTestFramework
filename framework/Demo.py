# coding=utf-8
from framework.webui_autotest_init import WebUI_Framework
from selenium import webdriver
import yaml

# # 基于关键字驱动实现的测试框架Demo，类似于RF
# wf = WebUI_Framework('Chrome')
# wf.visit('http://www.baidu.com')
# wf.input('id', 'kw', '测码学院')
# wf.click('id', 'su')
# class a:
#     def func(self, a, b):
#         return a + b
#
#
# args = WebUI_Framework.quit.__code__.co_argcount
# print(args)
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# driver.save_screenshot('../test.png')

file = open('../config/data.yaml', 'r', encoding='utf-8')
dic = yaml.load(stream=file, Loader=yaml.FullLoader)
print(dic)
