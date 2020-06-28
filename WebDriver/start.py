# This python code enables a user to auto webclock in and clock out of keka timesheet tool daily if setup properly


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

# file_absolute_paths
reasonFilePath = r"F:\Learn\Train\Python\WebDriver\reasonFile.txt"
userpassFilePath = r"F:\Learn\Train\userpassFile.txt"
chromedriverPath = r"F:\Learn\Train\Python\WebDriver\chromedriver.exe"


def generateReason():
    rea = open(reasonFilePath, "r")
    reason = rea.readlines()
    rea.close()
    return reason


driver = webdriver.Chrome(executable_path=chromedriverPath)
driver.get("https://app.keka.com/account/login")

reason = generateReason()

# add details in the text file as shown
# first line - username
# second line - password
# third line - domain name

userpassfile = open(userpassFilePath, "r")
for i, line in enumerate(userpassfile):
    if i == 0:
        userName = line.rstrip()
    if i == 1:
        passWord = line.rstrip()
    if i == 2:
        domainName = line.rstrip()
userpassfile.close()

userName_textBox_xpath = '//*[@id="email"]'
loginButton_xpath = '//*[@id="login-container-center"]/div/div/form/div/div[2]/div/button'
domainName_textBox_xpath = '//*[@id="subdomainname"]'
passWord_textBox_xpath = '//*[@id="password"]'
loginButton_xpath2 = '//*[@id="login-container-center"]/div/div/form/div/div[4]/div/button'
meMenu_xpath = '//*[@id="accordion"]/li[2]/a/span[1]'
attendanceTab_xpath = '/html/body/xhr-app-root/div/employee-me/div/ul/li[3]/a'
webClockIn_xpath = '/html/body/xhr-app-root/div/employee-me/div/employee-attendance/div/div/div/employee-attendance-stats/div/div[3]/employee-attendance-request-actions/div/div/div/div/div[2]/div/div[1]/a'
start_comment_xpath = '/html/body/modal-container/div/div/xhr-confirm-dialog/div[2]/form/div/textarea'
start_submit_xpath = '/html/body/modal-container/div/div/xhr-confirm-dialog/div[3]/button[2]'

driver.find_element_by_xpath(userName_textBox_xpath).send_keys(userName)
driver.find_element_by_xpath(loginButton_xpath).click()
driver.find_element_by_xpath(domainName_textBox_xpath).send_keys(domainName)
driver.find_element_by_xpath(passWord_textBox_xpath).send_keys(passWord)
driver.find_element_by_xpath(loginButton_xpath2).click()

WebDriverWait(driver, 100).until(
    ExpectedConditions.element_to_be_clickable((By.XPATH, meMenu_xpath)))

driver.find_element_by_xpath(meMenu_xpath).click()
driver.find_element_by_xpath(attendanceTab_xpath).click()
WebDriverWait(driver, 100).until(
    ExpectedConditions.element_to_be_clickable((By.XPATH, webClockIn_xpath)))
driver.find_element_by_xpath(webClockIn_xpath).click()
WebDriverWait(driver, 100).until(
    ExpectedConditions.element_to_be_clickable((By.XPATH, start_comment_xpath)))
driver.find_element_by_xpath(start_comment_xpath).send_keys(reason)
