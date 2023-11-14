import pytest
from fixture.application import Application
import json
import os.path
import importlib
import ftputil

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture(scope="session")
def configur(request):
    return load_config(request.config.getoption("--target"))

@pytest.fixture
def app(request, configur):
    global fixture
    browser = request.config.getoption("--browser")
    #web_config = configur["web"]
    #base_url = request.config.getoption("--baseUrl")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=configur["web"]['baseUrl'])
    #fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    fixture.session.ensure_login(username=configur["webadmin"]["username"], password=configur["webadmin"]["password"])
    return fixture


#@pytest.fixture(scope="session", autouse=True)
#def configure_server(request, configur):
#    install_server_configuration(configur["ftp"]["host"], configur["ftp"]["username"], configur["ftp"]["password"])
#    def fin():
#        restore_server_configuration(configur["ftp"]["host"], configur["ftp"]["username"], configur["ftp"]["password"])
#    request.addfinalizer(fin)


#def install_server_configuration(host, username, password):
#    with ftputil.FTPHost(host, username, password) as remote:
#        if remote.path.isfile("config_inc.php.bak"):
#            remote.remove("config_inc.php.bak")
#        if remote.path.isfile("config_inc.php"):
#            remote.rename("config_inc.php", "config_inc.php.bak")
#        remote.upload(os.path.join(os.path.dirname(__file__), "resources/config_inc.php"), "config_inc.php")


#def restore_server_configuration(host, username, password):
#    with ftputil.FTPHost(host, username, password) as remote:
#        if remote.path.isfile("config_inc.php.bak"):
#            if remote.path.isfile("config_inc.php"):
#                remote.remove("config_inc.php")
#            remote.rename("config_inc.php.bak", "config_inc.php")

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

