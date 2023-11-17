from model.project import Project
import string
import random


def random_name(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    proj = Project(name=random_name("Project", 5))
    old_proj = app.soap.project_list()
    app.project.add_project(proj)
    new_proj = app.soap.project_list()
    old_proj.append(proj.name)
    assert sorted(old_proj) == sorted(new_proj)