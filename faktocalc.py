from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QLabel,QWidget,QPushButton
import sys

def fak():
    sayi = int(txtSayi.text())
    carpim=1
    for i in range(1,sayi+1):
        carpim = carpim * i
    txtSonuc.setText(str(carpim))

app =QApplication([])
win = QWidget()
win.setWindowTitle("Faktoriyel Hesaplama")


lyt = QVBoxLayout()

txtSayi= QLineEdit()
lyt.addWidget(txtSayi)

txtSonuc= QLabel()
lyt.addWidget(txtSonuc)

btn=QPushButton()
btn.setText("Çarpım")
btn.clicked.connect(fak)
lyt.addWidget(btn)

win.setLayout(lyt)
win.show()
sys.exit(app.exec())