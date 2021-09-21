import xlUtils
from selenium import webdriver

driver=webdriver.Chrome("C:\\Users\R051705030\PycharmProjects\seleniumPython\Driver\chromedriver.exe")
driver.get("https://192.168.101.23/admin/")
driver.maximize_window()

file="C://Users/R051705030/Desktop/python/Automation/cb.xlsx"

rows=xlUtils.getRowCount(file,'Sheet1')

for r in range(2,rows+1):
    username=xlUtils.readData(file,"Sheet1",r,1)
    password=xlUtils.readData(file,"Sheet1",r,2)

    driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(username)
    driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(password)
    driver.find_element_by_xpath("//button[normalize-space()='SIGN IN']").click()

if driver.title != "Cashbaba Admin Panel":
    print("test failed")
    xlUtils.writeData(file,"Sheet1",r,3,"test failed")

else:
    print("Test is passed")
    xlUtils.writeData(file,"Sheet1",r, 3,"test passed")