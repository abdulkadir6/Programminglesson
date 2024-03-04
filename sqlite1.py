import sqlite3
db = sqlite3.connect("notlar.db")
imlec=db.cursor()
imlec.execute("select * from notlar order by Final desc")
veriler = imlec.fetchmany(2)
toplam=0
ogrsayi =0
for i in veriler:
    toplam += int(i[4])
    ogrsayi +=1
print(toplam/ogrsayi)
db.close() 