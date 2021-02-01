from selenium import webdriver
class loginPage:

    # def __init__(self):
    #     self.driver = webdriver.Chrome(executable_path=r"C:\Deepak\SeleniumFramework\chromedriver_win32\chromedriver.exe")
    #     self.driver.maximize_window()

    def login_to_page(self):
        self.driver.implicitly_wait(5)
        self.driver.get("http://the-internet.herokuapp.com/")

    def click(self):
        print("deepak")