import sys, requests, json, configparser
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from template import *
from login import *
from linkbox import *
from cryptography.fernet import Fernet

class Cypher(object):
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read('keys.ini')

    def encrypt(self, val):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
            
        f = Fernet(key)
        encoded = f.encrypt(str(val).encode())
        self.__config['auth']={
            'token': encoded.decode('utf-8')
        }
        
        with open('keys.ini', 'w') as configfile:
            self.__config.write(configfile)
        
       
    def get_auth(self):
        token = self.__config.get('auth', 'token').encode()
        key = open("secret.key", "rb").read()
        f = Fernet(key)
        return f.decrypt(token).decode('utf-8')

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.gridLayout.setColumnStretch(0,3)
        self.setStyleSheet(open('dialogstyle.css').read())
        self.ui.fetch.clicked.connect(self.loadpg)
        self.show()

    def loadpg(self):
        try:
            cypher = Cypher()
            header = {"Authorization": "Token {}".format(cypher.get_auth())}
            response = requests.post('http://127.0.0.1:8000/test/', json={'link':self.ui.URL.text()}, headers = header)
            linkui = LinkView()
            linkui.ui.URL_gen.setText(response.text)
            linkui.exec_()
        except configparser.NoSectionError:
            linkui = LinkView()
            linkui.ui.URL_gen.setText('Pls Login First')
            linkui.exec_()

class LoginView(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.login.setDefault(True)
        self.ui.login.clicked.connect(self.get_login)
        self.ui.sign_up.clicked.connect(self.signup)
        self.setStyleSheet(open('loginstyle.css').read())
        self.show()

    def get_login(self):
        response = requests.post('http://127.0.0.1:8000/login/', json={'username':self.ui.uname.text(), 'password': self.ui.pwd.text()})
        json_resp = json.loads(response.text)
        if "token" in json_resp:
            cypher = Cypher()
            cypher.encrypt(json_resp['token'])

        else:
            self.ui.label_3.setText("Oops")

        return None

    def signup(self):
        return None

class LinkView(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Link()
        self.ui.setupUi(self)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())