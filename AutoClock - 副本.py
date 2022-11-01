#引入selenium库中的 webdriver 模块
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)


options.add_experimental_option('mobileEmulation',{'deviceName':'iPhone X'})
#打开谷歌浏览器
#打开百度搜索主页
driver.get('http://yiqing.ctgu.edu.cn/wx/index/login.do')

#身份证号
xh= ''
#对应的密码
password = ''

#driver.find_element_by_id('username1').send_keys(xh)
driver.find_element(By.ID,'username1').send_keys(xh)
driver.find_element(By.ID,'password1').send_keys(password)
driver.find_element(By.XPATH,'/html/body/main/section[2]/form/div[3]/input').click()
#完成登录

print("等候ing")
time.sleep(1)
print("结束等候")
driver.find_element(By.TAG_NAME,'button').click()
#定位
# driver.find_element_by_id('open_popup').click()

path = driver.find_element(By.XPATH,'//*[@id="szdz"]')

driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",path,'value','湖北省 宜昌市 西陵区')



time.sleep(2)
#点击提交按钮
driver.find_element(By.ID,'submit_btn').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/a[2]').click()
print("上报成功")
# frame1 = driver.find_element_by_css_selector(".fixed-top bg-white ai-padding fit_768")
# driver.switch_to_frame(frame1)
