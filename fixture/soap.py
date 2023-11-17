from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        #client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except  WebFault:
            return False

    def project_list(self):
        #client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        client = Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            a = []
            b = client.service.mc_projects_get_user_accessible(username=self.app.configur["webadmin"]["username"],
                                     password=self.app.configur["webadmin"]["password"])
            for i in range(len(b)):
                a.append(b[i]["name"])
            return list(a)
        except WebFault:
            return False