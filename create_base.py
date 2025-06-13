import sqlite3
import os


dirname=os.path.dirname(__file__)
os.chdir(dirname)

connection = sqlite3.connect("base.db")

cursor = connection.cursor() 
  
cursor.execute("CREATE TABLE IF NOT EXISTS tab_3(ID INTEGER PRIMARY KEY AUTOINCREMENT,№ТС TEXT, МАРКА TEXT, НАЗВАНИЕ TEXT, ФИО TEXT)")
pipls=(("м256ео", "Toyta", "Sienta","Шевчук В.И."),("м457вм", "Honda", "Honda Accord","Вернер Р.Н."),("в785сс", "Mazda", "Mazda 787B","Ревнивцев О.К."),("в555вв", "Nissan", "Almera Classic","Амиров С.Л."),("к345нр", "Volkswagen", "Caddy","Троцев А.П."))
cursor.executemany("INSERT INTO tab_3(№ТС,МАРКА,НАЗВАНИЕ,ФИО) VALUES(?,?,?,?)",pipls)
connection.commit()
 
 
cursor.execute("CREATE TABLE IF NOT EXISTS tab_2(ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
users=(("Администратор","123"),("Пользователь",  "111"))
cursor.executemany("INSERT INTO tab_2 (username, password) VALUES (?, ?)", users)
connection.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS tab_4(НАРУШЕНИЕ TEXT,ДАТА TEXT, СУММА TEXT)")
shtraf=(("превышение скорости", "15.06.2009", "1500"),("проезд на красный", "23.03.2024", "1000"),("езда в нетрезвом состоянии", "30.08.2025", "5000"),("нарушение правил парковки", "27.02.2003", "500"))
cursor.executemany("INSERT INTO tab_4(НАРУШЕНИЕ,ДАТА, СУММА) VALUES(?,?,?)",shtraf)
connection.commit()

connection.close()






