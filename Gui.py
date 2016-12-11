import sys
from PyQt4 import QtGui
import codecs
from OCMID import ImageDownloader

class Window(QtGui.QWidget):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle('O.C.I.M.D')
        self.setGeometry(150,100,500,300)
        #self.setWindowIcon(QtGui.QIcon('image.png'))
        self.Home()

    def Home(self):
        enter_url = QtGui.QLineEdit()
        enter_url.textChanged.connect(self.url_submitted)
        enter_url.resize(300,20)
        enter_url.move(50,75)

        layout = QtGui.QFormLayout()
        layout.addRow("Enter URL",enter_url)

        btn = QtGui.QPushButton("Start Download")
        btn.clicked.connect(self.url_downloader)

        self.setLayout(layout)


        self.show()

    def url_downloader(self):
        ImageDownloader()


    def url_submitted(self,text):
        with codecs.open('data.txt','w','utf-8') as text_file:
            text_file.write("%s" %text)

def main():
    app = QtGui.QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
main()
