import sys, requests, json
from PyQt5.QtWidgets import QDialog, QApplication, QAbstractItemView, QTableWidgetItem, QHeaderView, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QThreadPool, QCoreApplication, Qt, QTimer
from PyQt5.QtGui import QMovie
from template import *
from login import *
from loader import *
from key_manager import Cypher
from worker import Worker

cypher = Cypher()

class Loader(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Loader()
        self.ui.setupUi(self)
        self.ui.movie_label.setScaledContents(True)
        self.setWindowFlags(Qt.FramelessWindowHint| Qt.WindowStaysOnTopHint | Qt.BypassWindowManagerHint)
        self.movie = QMovie('loader2.gif')
        self.ui.movie_label.setMovie(self.movie)
        self.movie.start()

class MainView(QDialog):
    def __init__(self):
        super().__init__()
        self.__resp = {}
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        if not cypher.get_auth():
            login = LoginView()
            login.exec_()
    
        if cypher.get_auth():    
            
            self.ui.single.setChecked(True)
            self.ui.stic.setChecked(True)
            self.ui.json.setChecked(True)
            self.threadpool = QThreadPool()
            self.loader = Loader()

            # Grid Setup
            self.ui.gridLayout.setColumnStretch(0,3)
            self.ui.gridLayout_2.setColumnStretch(0,1)
            
            # Table Setup
            self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.ui.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
            self.ui.listWidget.itemSelectionChanged.connect(self.displaytb)
            self.ui.fetch.clicked.connect(self.fetch)
            self.show()
        
        else:
            sys.exit()

    def fetch(self):
        worker = Worker(self.loadpg)
        worker.signals.finished.connect(self.destroy_loader)
        self.threadpool.start(worker)
        self.show_loader()

    def show_loader(self):
        self.loader.ui.tag.setText("Processing")
        self.loader.setWindowModality(Qt.ApplicationModal)
        self.loader.show()

    def destroy_loader(self):
        self.loader.close()
       
    def loadpg(self):
        auth_key = cypher.get_auth()
        if auth_key:
            header = {"Authorization": "Token {}".format(cypher.get_auth())}
            try:
                response = requests.post('http://127.0.0.1:8000/link_detail/', json={'link':self.ui.URL.text()}, headers = header, timeout = 10)
                tmp = json.loads(response.text)
                if "data" in tmp:
                    for i in tmp["data"]:
                        key = list(i.keys())[0]
                        self.__resp[key] = i[key]
                        self.ui.Info.setText("Found {} table(s) in the given link.".format(len(self.__resp)))
                        self.ui.listWidget.clear()
                        self.ui.listWidget.addItems(self.__resp.keys())
                
                elif "error" in tmp:
                        self.ui.Info.setText(tmp["error"])
            except requests.ConnectionError:
                self.ui.Info.setText("Failed to Establish Connection")

            except requests.ConnectTimeout:
                self.ui.Info.setText("Connection Timout")

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
        self.loader = Loader()
        self.ui.setupUi(self)
        self.ui.error_frm.hide()
        self.threadpool = QThreadPool()
        self.ui.login.setDefault(True)
        self.ui.login.clicked.connect(self.login)
        self.ui.sign_up.clicked.connect(self.signup)
        self.ui.pushButton.clicked.connect(self.ui.error_frm.hide)
        self.setStyleSheet(open('styles/loginstyle.css').read())
        self.show()

    def login(self):
        worker = Worker(self.get_token)
        worker.signals.finished.connect(self.destroy_loader)
        self.threadpool.start(worker)
        self.show_loader()
   
    def get_token(self):
        try:
            response = requests.post('http://127.0.0.1:8000/login/', json={'username':self.ui.uname.text(), 'password': self.ui.pwd.text()})
            if response.status_code == 200:
                json_resp = json.loads(response.text)
                if "token" in json_resp:
                    cypher.encrypt(json_resp['token'])
                    self.close()

            if response.status_code == 400:
                self.ui.error_frm.show()

        except (requests.ConnectionError, requests.ConnectTimeout):
            self.ui.label_3.setText("Connection Error")


    def signup(self):
        return None

    def show_loader(self):
        self.loader.ui.tag.setText("Logging In")
        self.loader.setWindowModality(Qt.ApplicationModal)
        self.loader.show()

    def destroy_loader(self):
        self.loader.close()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainView()
    w.show()
    sys.exit(app.exec_())