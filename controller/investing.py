from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
from bs4 import BeautifulSoup


class Investing(object):
    def __init__(self,tickers:list):
        self.tickers = tickers
        path_project = os.path.abspath(os.path.dirname(sys.argv[0]))
        path_webdriver = path_project + "/utils/webdriver/chromedriver"
        PHANTOMJS_CAP = webdriver.DesiredCapabilities.PHANTOMJS.copy()
        PHANTOMJS_CAP['load-images'] = False
        PHANTOMJS_CAP['disk_cache'] = False
        #self.driver = webdriver.PhantomJS(executable_path=path_webdriver,
        #                             desired_capabilities=PHANTOMJS_CAP)
        self.driver = webdriver.Chrome(executable_path=path_webdriver)
        print("Inicio scraper")

    def start(self):

        self.driver.get("https://es.investing.com/")
        self.driver.find_element_by_class_name("popupCloseIcon").click()
        search_field = self.driver.find_element_by_id("combineSearchFormTop")
