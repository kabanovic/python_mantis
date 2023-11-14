from selenium import webdriver
from fixture.session import Session
from fixture.project import ProjectHelper
from selenium.webdriver.common.by import By

class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = Session(self)
        self.base_url = base_url
        self.project = ProjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if wd.current_url.endswith("/index.php"):
            return
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()