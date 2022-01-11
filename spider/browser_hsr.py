from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
driver = webdriver.Chrome()     # 打开 Chrome 浏览器


driver.get("https://m.thsrc.com.tw/tw/TimeTable/SearchResult")

driver.find_element_by_xpath("//button[@class='swal2-confirm swal2-styled']").click()
#print(driver.page_source)
start= Select(driver.find_element_by_name("startStation"))
#輸入內容
start.select_by_value("f2519629-5973-4d08-913b-479cce78a356")
#提交表單台北
end = Select(driver.find_element_by_name("endStation"))
end.select_by_value("977abb69-413a-4ccf-a109-0272c24fd490")
time = Select(driver.find_element_by_name("timeSelect"))
time.select_by_visible_text("13:00")
driver.find_element_by_css_selector("[class='sendTimeCheck ui-link']").click()

soup=BeautifulSoup(driver.page_source,'html.parser')
big_c=soup.select("div.timeResultList.ui-grid-b")
#print(big_c)
for x in big_c:
    for i in x.select("div"):
         print(i.text.replace(" ","").replace("<br>","") ) 
driver.quit()


