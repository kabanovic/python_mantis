from selenium.webdriver.common.by import By
from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.open_projects()
        wd.find_element(By.XPATH, "//input[@value='Create New Project']").click()
        self.fill_name_project(project)
        wd.find_element(By.XPATH, "//input[@value='Add Project']").click()
        self.return_main()
        self.project_cache = None

    def open_projects(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'Manage').click()
        wd.find_element(By.LINK_TEXT, 'Manage Projects').click()

    def return_main(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'My View').click()

    def fill_name_project(self, project):
        wd = self.app.wd
        wd.find_element(By.NAME, "name").clear()
        wd.find_element(By.NAME, "name").send_keys(project.name)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_projects()
            self.project_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "table.width100 tr.row-1, table.width100 tr.row-2"):
                #text = element.text
                proj = element.find_elements(By.TAG_NAME, "td")
                name = proj[0].text
                self.project_cache.append(Project(name=name))
        return list(self.project_cache)

