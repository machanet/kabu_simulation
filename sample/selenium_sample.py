＃ this program cannot run without chromedriver ＆ selenium
# If you want to run this program, you shold run above commands
#
# pip install selenium
# brew cask install chromedriver
#

from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get('http://jp.kabumap.com/servlets/kabumap/Action?SRC=basic/top/base&codetext=7203')
unit = driver.find_element_by_css_selector('#minUnit').text
print(unit)
