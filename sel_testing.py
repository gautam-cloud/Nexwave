#Open browser
#Type url
#find field
#type user,pass
#press enter
#verify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome()#Download ChromeDriver and extract and keep it in bin
browser.get('http://192.168.3.68:8080/login')
user_field=browser.find_element_by_name('uname')
pass_field=browser.find_element_by_name('pw')
user_field.send_keys('abc')
pass_field.send_keys('xyz')
pass_field.send_keys(Keys.RETURN)#this is for Press Enter
try:
    assert 'Log' in browser.title
    print('Testcase success')
except AssertionError:
    print('Test Failed')
finally:
    import time
    time.sleep(2)
    browser.close()

import unittest
 #unitest is a framework
class MyTests(unittest.TestCase):
    #Setup->Testcase->TearDown
    def setUp(self):
        self.browser=webdriver.Chrome()
        print('In Setup....')
    def test_testcase1(self):
        browser=self.browser
        browser.get('http://192.168.3.68:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)  # this is for Press Enter
        assert 'Log' in browser.title

    def test_testcase2(self):
        browser = self.browser
        browser.get('http://192.168.3.68:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)  # this is for Press Enter
        assert 'Log' in browser.title

    def test_testcase3(self):
        browser = self.browser
        browser.get('http://192.168.3.68:8080/login')
        user_field = browser.find_element_by_name('uname')
        pass_field = browser.find_element_by_name('pw')
        user_field.send_keys('abc')
        pass_field.send_keys('xyz')
        pass_field.send_keys(Keys.RETURN)  # this is for Press Enter
        assert 'Log' in browser.title

    def tearDown(self):
        print('In TearDown...')
        import time
        time.sleep(2)
        self.browser.close()

if __name__=='__main__':
    if __name__ == '__main__':
        unittest.main()
