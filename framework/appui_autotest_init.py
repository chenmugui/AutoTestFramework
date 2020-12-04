from appium import webdriver

desired_capabilities = {}
desired_capabilities['deviceName'] = '127.0.0.1:62001'
desired_capabilities['platformName'] = 'Android'
desired_capabilities['platformVersion'] = '5.1.1'
desired_capabilities['appPackage'] = 'com.tencent.mobileqq'
desired_capabilities['appActivity'] = '.activity.SplashActivity'
desired_capabilities['noReset'] = True
desired_capabilities['aotumationName'] = 'uiAutomator1'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_capabilities)
