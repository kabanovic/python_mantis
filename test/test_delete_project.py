from model.project import Project
import random


def test_add_project(app):
    #app.session.login("administrator", "root")
    if len(app.project.get_project_list()) == 0:
        app.project.add_project(Project(name="Project1"))
    old_proj = app.soap.project_list(username=app.configur["webadmin"]["username"],
                                     password=app.configur["webadmin"]["password"])
    proj = random.choice(old_proj)
    app.project.del_project(proj)
    new_proj = app.soap.project_list(username=app.configur["webadmin"]["username"],
                                     password=app.configur["webadmin"]["password"])
    old_proj.remove(proj)
    assert sorted(old_proj) == sorted(new_proj)