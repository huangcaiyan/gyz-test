from selenium import webdriver
import time
# from base.public_page import PublicPage

class InvoicePage:

    # invoiceType:发票类型
    def __init__(self,driver,invoiceType):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.invoiceType = invoiceType
        

    # 去发票列表
    def go_to_invoice_list(self,base_url):
        self.driver.get(base_url + '/app/invoice/'+self.invoiceType+'-invoice')
        time.sleep(3)
        

