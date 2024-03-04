from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QTextEdit
from PyQt5.QtGui import QFont
import sys

def window():
    app = QApplication(sys.argv)
    win= QMainWindow()
    win.setWindowTitle("İlk Uygulamamız")
    win.setGeometry(600,250,500,500)

    lblBaslik = QLabel(win)
    lblBaslik.setText("Stok Kartı")
    lblBaslik.setFont(QFont("Arial",25,2,False))
    lblBaslik.setStyleSheet("color:blue")
    lblBaslik.setGeometry(200,0,500,50)

    lblStoKKodu = QLabel(win)
    lblStoKKodu.setText("Stok Kodu")
    lblStoKKodu.setFont(QFont("Arial",15,10,False))
    lblStoKKodu.setStyleSheet("color:black")
    lblStoKKodu.setGeometry(50,50,500,50)

    txtStokKodu = QTextEdit(win)
    txtStokKodu.setFont(QFont("Arial",15,10,False))
    txtStokKodu.setToolTip("Buraya Stok Kodu Giriniz!")
    txtStokKodu.setStyleSheet("color:black")
    txtStokKodu.setGeometry(150,50,300,40)
    


    win.show()
    sys.exit(app.exec())

window()
