import sys, requests, json
from PyQt5.QtWidgets import QDialog, QApplication, QAbstractItemView, QTableWidgetItem, QHeaderView
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QThreadPool, QCoreApplication
from template import *
from login import *
from linkbox import *
from key_manager import Cypher
from worker import Worker

class MainView(QDialog):
    def __init__(self):
        super().__init__()
        self.__resp = {}
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        self.setStyleSheet(open('styles/dialogstyle.css').read())
        self.ui.ctrl_frame.setDisabled(True)

        # Grid Setup
        self.ui.gridLayout.setColumnStretch(0,3)
        self.ui.gridLayout_2.setColumnStretch(0,1)
        
        # Table Setup
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.listWidget.itemSelectionChanged.connect(self.displaytb)
        self.ui.fetch.clicked.connect(self.loader)
        self.show()

    def loader(self):
        worker = Worker(self.loadpg)
        self.threadpool.start(worker)
       
    def loadpg(self):
        cypher = Cypher()
        auth_key = cypher.get_auth()
        if auth_key:
            header = {"Authorization": "Token {}".format(cypher.get_auth())}
            response = requests.post('http://127.0.0.1:8000/link_detail/', json={'link':self.ui.URL.text()}, headers = header)
            tmp = json.loads(response.text)["Data"]
            for i in tmp:
                key = list(i.keys())[0]
                self.__resp[key] = i[key]
            self.ui.Info.setText("Found {} table(s) in the given link.".format(len(self.__resp)))
            self.ui.listWidget.addItems(self.__resp.keys())
        else:
            self.ui.Info.setText("Unauthorized")

    def displaytb(self):
        table_data = self.__resp[self.ui.listWidget.currentItem().text()]
        tmp = 0
        self.ui.tableWidget.setColumnCount(len(table_data[0].keys()))
        self.ui.tableWidget.setRowCount(len(table_data))
        for i in range(len(table_data)):
            tmp = 0
            for key, value in table_data[i].items():
                self.ui.tableWidget.setItem(i, tmp, QTableWidgetItem(value))
                tmp += 1

        self.ui.tableWidget.setHorizontalHeaderLabels(list(table_data[0].keys()))

class LoginView(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.__status = ''
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        self.ui.login.setDefault(True)
        self.ui.login.clicked.connect(self.login)
        self.ui.sign_up.clicked.connect(self.signup)
        self.setStyleSheet(open('styles/loginstyle.css').read())
        self.show()

    def login(self):
        worker = Worker(self.get_token)
        self.threadpool.start(worker)
       
    def get_token(self):
        response = requests.post('http://127.0.0.1:8000/login/', json={'username':self.ui.uname.text(), 'password': self.ui.pwd.text()})
        json_resp = json.loads(response.text)
        if "token" in json_resp:
            cypher = Cypher()
            cypher.encrypt(json_resp['token'])

        else:
            self.ui.label_3.setText("Oops")
        self.__status = 'done'

    def signup(self):
        return None

class LinkView(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Link()
        self.ui.setupUi(self)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = LoginView()
    w.show()
    sys.exit(app.exec_())