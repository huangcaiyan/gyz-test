from selenium import webdriver
import time
import pandas as pd

file = pd.read_excel(
    '/Users/huangcaiyan/work/guanplus-test/test_case/excel_read/result.xls')

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 由file的第二列创建个列表
search_results = list(file.iloc[:; 1])


def search_keyword(word):
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys(word)
    driver.find_element_by_id('su').click()

    times.sleep(2)
    result = driver.find_element_by_xpath(".//*[@id='2']/h3/a").text
    return result


# 遍历第一列
for index, word in enumerate(list(file.iloc[:, 0])):
    # 把搜索结果写入list
    search_results[index] = search_keyword(word)
# 把list写入df
file.iloc[:, 1] = search_results
# 把df另存为excel
file.to_excel("search_results.xlsx", index=False)
