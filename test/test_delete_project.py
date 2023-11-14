from model.project import Project
import random


def test_add_project(app):
    #app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.add_project(Project(name="Project1"))
    old_projects = app.project.get_project_list()
    proj = random.choice(old_projects)
    app.project.del_project(proj)
    new_projects = app.project.get_project_list()
    old_projects.remove(proj)
    assert sorted(old_projects, key=Project.name_or_not) == sorted(new_projects, key=Project.name_or_not)