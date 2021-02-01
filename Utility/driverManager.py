
import logging
import pytest

from selenium import webdriver

logging.basicConfig(format='%(asctime)s,-%(levelname)s-%(message)s',level=logging.INFO)

class deviceManager:

    def setup_class(self):
        logging.info("opening chrome browser")
        self.driver=webdriver.Chrome(executable_path=r"C:\Deepak\SeleniumFramework\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://the-internet.herokuapp.com/")


    def teardown_class(self):
        print("TearDown")
        logging.info("closing chrom browser")
        self.driver.quit()

if __name__ == '__main__':
    obj=deviceManager()
    obj.setup_class()
    obj.teardown_class()

