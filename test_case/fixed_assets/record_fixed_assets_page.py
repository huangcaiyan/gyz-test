from selenium import webdriver
import time
from base.public_page import PublicPage 
from config import Config

class RecordFixedAssetsPage(object):

    def __init__(self,driver):
        self.driver = webdriver.Chrome()
        self.driver = driver 