from model.project import Project
import string
import random


def random_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    proj = Project(name=random_name("name", 10))
    old_projects = app.project.get_project_list()
    app.project.add_project(proj)
    new_projects = app.project.get_project_list()
    old_projects.append(proj)
    assert sorted(old_projects, key=Project.name_or_not) == sorted(new_projects, key=Project.name_or_not)