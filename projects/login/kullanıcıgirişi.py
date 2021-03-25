import sys
import sqlite3
from PyQt5 import QtWidgets,QtGui

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.baglanti()
        self.init_ui()


    def baglanti(self):

        self.baglanti = sqlite3.connect("veritabanı.db")

        self.cursor = self.baglanti.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bilgiler (kullanıcı_adı TEXT,parola TEXT)")

        self.baglanti.commit()

    def init_ui(self):

        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("")
        self.kayit = QtWidgets.QPushButton("Kayıt Ol")
        self.sil = QtWidgets.QPushButton("Kayıt Sil")
        self.forget = QtWidgets.QPushButton("Şifremi Unuttum")

        y = QtWidgets.QVBoxLayout()
        y.addWidget(self.kullanici_adi)
        y.addWidget(self.parola)
        y.addWidget(self.yazi_alani)
        y.addStretch()
        y.addWidget(self.sil)
        y.addWidget(self.forget)
        y.addWidget(self.kayit)
        y.addWidget(self.giris)

        x = QtWidgets.QHBoxLayout()
        x.addStretch()
        x.addLayout(y)
        x.addStretch()

        self.setLayout(x)

        self.giris.clicked.connect(self.login)
        self.kayit.clicked.connect(self.register)
        self.sil.clicked.connect(self.delete)
        self.forget.clicked.connect(self.unut)

        self.setWindowTitle("Kullanıcı Girişi")

        self.show()

    def login(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("Select * From bilgiler where kullanıcı_adı = ? and parola = ? " , (adi,par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.yazi_alani.setText("kullanıcı adınız veya şifreniz yanlış belki de kayıtlı değilsiniz\nama hangisi olduğunu söylemem")


        else:
            self.yazi_alani.setText("hoşgeldiniz " +  adi)

    def register(self):

        ad = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("insert into bilgiler values(?,?)",(ad,par))
        self.baglanti.commit()

        self.yazi_alani.setText("Aramıza hoşgeldin " + ad)

    def delete(self):

        ad = self.kullanici_adi.text()
        par = self.parola.text()

        self.cursor.execute("delete from bilgiler where kullanıcı_adı = ? and parola = ?",(ad,par))
        self.baglanti.commit()

        self.yazi_alani.setText("Güle güle " + ad)

    def unut(self):

        self.yazi_alani.setText("Lütfen kullanıcı adınızı giriniz!")
        ad = self.kullanici_adi.text()
        self.cursor.execute("select * from bilgiler where kullanıcı_adı = ?", (ad,) )
        x = self.cursor.fetchall()
        self.yazi_alani.setText("Bilgileriniz\n" + x[0][0] + "\n" + x[0][1])




app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

