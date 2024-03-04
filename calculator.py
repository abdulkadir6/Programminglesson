from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QVBoxLayout,QLabel,QWidget,QPushButton,QHBoxLayout
import sys

#region fonksiyonlar
def carp():
    sayi1 = int(txtSayi1.text())
    sayi2 = int(txtSayi2.text())
    txtSonuc.setText(str(sayi1*sayi2))

def topla():
    sayi1 = int(txtSayi1.text())
    sayi2 = int(txtSayi2.text())
    txtSonuc.setText(str(sayi1+sayi2))

def cikar():
    sayi1 = int(txtSayi1.text())
    sayi2 = int(txtSayi2.text())
    txtSonuc.setText(str(sayi1-sayi2))

def bol():
    sayi1 = int(txtSayi1.text())
    sayi2 = int(txtSayi2.text())
    txtSonuc.setText(str(sayi1/sayi2))
#endregion

app =QApplication([])
win = QWidget()
win.setWindowTitle("İlk Program")

lyt = QVBoxLayout()

txtSayi1= QLineEdit()
lyt.addWidget(txtSayi1)

txtSayi2= QLineEdit()
lyt.addWidget(txtSayi2)

txtSonuc= QLineEdit()
txtSonuc.setEnabled(False)
lyt.addWidget(txtSonuc)

lyt2 = QHBoxLayout()

btn=QPushButton()
btn.setText("Çarpım")
btn.clicked.connect(carp)
lyt2.addWidget(btn)

btn2=QPushButton("Topla")
btn2.clicked.connect(topla)
lyt2.addWidget(btn2)

btn3=QPushButton("Cikar")
btn3.clicked.connect(cikar)
lyt2.addWidget(btn3)

btn4=QPushButton("Böl")
btn4.clicked.connect(bol)
lyt2.addWidget(btn4)

lyt.addLayout(lyt2)

win.setLayout(lyt)
win.show()
sys.exit(app.exec())
