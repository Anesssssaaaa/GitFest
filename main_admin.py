from tkinter import ttk
from tkinter import *
from data import del_data, add_data, edit_data
import os
import datetime
import sqlite3
   
def on_closing():
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Выключение ИС")
    log_file.close()
    connection.close()
    tk.destroy()
 
 


dirname=os.path.dirname(__file__)
os.chdir(dirname)


if not os.path.exists("log"):
    os.mkdir("log")

now=datetime.datetime.now()
name = now.strftime("%d.%m.%Y_%H.%M.%S")

log_file=open(rf"log\log_{name}.txt", 'w')



tk = Tk()
tk.title("Таблица")
tk.geometry("800x500+100+100")
tk.protocol("WM_DELETE_WINDOW", on_closing)
    
columns_tuple = ("ID", "t", "m", "n","f")
tree = ttk.Treeview(tk, columns=columns_tuple, show="headings")


def shtraf():
    roi = Tk()
    roi.title("ШТРАФЫ")
    roi.geometry("400x380+150+150")
    pop = ttk.Treeview(roi, show="headings")


    def chtraf1():
        v = e.get()
        d = e1.get()
        r = e2.get()
        
        cursor.execute("INSERT INTO tab_4 (НАРУШЕНИЕ, ДАТА, СУММА) VALUES (?, ?, ?)", ( v, d, r))
        connection.commit()
        for item in pop.get_children():
            pop.delete(item)
        cursor.execute("SELECT * FROM tab_4")
        shtraf = cursor.fetchall()
        connection.commit()    
        for v,d,r in shtraf:
            pop.insert("", END, values=(v,d,r))
    
    
        now=datetime.datetime.now()
        name = now.strftime("%d.%m.%Y_%H.%M.%S")
        log_file.write(f"{name} Запись {id} добавлена\n")        
       
        
        e.delete(0, END)
        e1.delete(0, END)
        e2.delete(0, END)

    def ud1():
        data = pop.item(pop.selection())
        data_ID=data["values"][2]
        cursor.execute(f"DELETE FROM tab_4 WHERE СУММА={data_ID}")
        connection.commit()

        for item in pop.get_children():
            pop.delete(item)
        cursor.execute("SELECT * FROM tab_4")
        shtraf = cursor.fetchall()
        connection.commit()    
        for d in shtraf:
            pop.insert('', END, values=d)
        
        now=datetime.datetime.now()
        name = now.strftime("%d.%m.%Y_%H.%M.%S")
        log_file.write(f"{name} Запись {data_ID} удалена\n")


    l=Label(roi,text="НАРУШЕНИЕ")
    l.place(x=20,y=250)

    l2=Label(roi,text="ДАТА")
    l2.place(x=20,y=280)

    l3=Label(roi,text="СУММА")
    l3.place(x=20,y=310)

    connection = sqlite3.connect("base.db")
    cursor = connection.cursor() 

    cursor.execute("SELECT * FROM tab_4")

    shtraf=cursor.fetchall()
    for data in shtraf:
        pop.insert("", END, values=data)
    connection.commit()

    


    e=Entry(roi,text="")
    e.place(x=125,y=250)

    e1=Entry(roi,text="")
    e1.place(x=55,y=280)

    e2=Entry(roi,text="")
    e2.place(x=70,y=310)


 
    b=Button(roi,text="ввод",command=chtraf1)
    b.place(x=320,y=270)

    
    b2=Button(roi,text="удалить",command=ud1)
    b2.place(x=320,y=300)
   


    pop["columns"] = ("v", "d", "r")


 

    pop.column("v", width=180)
    pop.column("d", width=180)
    pop.column("r", width=180)



    pop.heading("v", text="НАРУШЕНИЕ")
    pop.heading("d", text="ДАТА")
    pop.heading("r", text="СУММА")




    pop.heading("v", text="НАРУШЕНИЕ", anchor="center")
    pop.heading("d", text="ДАТА", anchor="center")
    pop.heading("r", text="СУММА", anchor="center")


    pop.column("v", width=120, anchor="w")  
    pop.column("d", width=90, anchor="w")
    pop.column("r", width=100, anchor="w")


    
    pop.pack(padx=5, pady=5)

    


    roi.mainloop()



tree.heading("ID", text="ID", anchor="center")
tree.heading("t", text="№ТС", anchor="center")
tree.heading("m", text="МАРКА", anchor="center")
tree.heading("n", text="НАЗВАНИЕ", anchor="center")
tree.heading("f", text="ФИО", anchor="center")


tree.column("ID", width=50, anchor="w")
tree.column("t", width=130, anchor="w") 
tree.column("m", width=100, anchor="w")
tree.column("n", width=250, anchor="w")
tree.column("f", width=250, anchor="w")



connection = sqlite3.connect("base.db")
cursor = connection.cursor() 

cursor.execute("SELECT * FROM tab_3")

pipls=cursor.fetchall()
connection.commit()

for data in pipls:
    tree.insert("", END, values=data) 


E_t=Entry(tk)
E_m=Entry(tk)
E_n=Entry(tk)
E_f=Entry(tk)

L_t=Label(tk, text="№ТС")
L_m=Label(tk, text="МАРКА")
L_n=Label(tk, text="НАЗВАНИЕ")
L_f=Label(tk, text="ФИО")

L_id=Label(tk, text="IID:")

B_Enter=Button(tk, text="Ввод", command=lambda: add_data(tree, E_t,E_m,E_n,E_f, log_file, connection, cursor))
B_del=Button(tk, text="Удалить", command=lambda: del_data(tree, log_file, connection, cursor))
B_edit=Button(tk, text="Изменить", command=lambda: edit_data(tree,log_file, E_t,E_m,E_n,E_f, L_id, B_del, B_edit, B_Enter, connection, cursor))
B_shtraf=Button(tk,text="ШТРАФЫ",command=shtraf)

tree.place(x=10, y=10, height=200)
L_id.place(x=100, y=240)

L_t.place(x=30, y=270)
L_m.place(x=30, y=300)
L_n.place(x=30, y=330)
L_f.place(x=30, y=360)

E_t.place(x=100, y=270, width=160)
E_m.place(x=100, y=300, width=160)
E_n.place(x=100, y=330, width=160)
E_f.place(x=100, y=360, width=160)

B_Enter.place(x=700, y=370, width=70)
B_del.place(x=700, y=410, width=70)
B_edit.place(x=700, y=450, width=70)
B_shtraf.place(x=700,y=330)

M=Menu(tk)

def nas():
    fyt = Tk()
    fyt.title("настройки")
    fyt.geometry("300x300+100+100")
    
    fyt.mainloop()


def dok():
    kik = Tk()
    kik.title("О программе")
    kik.geometry("1000x350+50+50")

    L1=Label(kik,text="Название программы: Учет о нарушениях ПДД")
    L2=Label(kik,text="Краткое описание:")


    L3=Label(kik,text="Данная программа представляет собой удобное и эффективное решение для управления системой.")
    L4=Label(kik,text="Она разработана на языке Python и использует встроенную базу данных SQLite для хранения и обработки информации о нарушениях правил дорожного движения.")
    L5=Label(kik,text="Программа предназначена для ГАИ.")

    L6=Label(kik,text="Основные функции:")
    L7=Label(kik,text="- Управление записями: ГАИшники могут добавлять, редактировать и удалять записи о штрафах, включая информацию о сумму, дате и виде нарушения.")
   
    L8=Label(kik,text="Технологии:")
    L9=Label(kik,text="- Язык программирования: Python")
    L10=Label(kik,text="- База данных: SQLite")
    L11=Label(kik,text="- Библиотеки: Используются библиотеки sqlite3 для работы с базой данных, а также другие сторонние библиотеки для реализации графического интерфейса (например, tkinter)")

    L12=Label(kik,text="Почему эта программа полезна:")
    L13=Label(kik,text="Программа нарушений упрощает процесс учёта нарушений ПДД, уменьшает риск потери информации и делает работу ГАИшников более организованной и эффективной.")
    


    L1.place(y=5,x=350)
    L2.place(y=35,x=70)
    L3.place(y=60,x=10)
    L4.place(y=80,x=10)
    L5.place(y=100,x=10)
    L6.place(y=135,x=70)
    L7.place(y=160,x=10)
    L8.place(y=185,x=70)
    L9.place(y=210,x=10)
    L10.place(y=230,x=10)
    L11.place(y=250,x=10)
    L12.place(y=285,x=70)
    L13.place(y=310,x=10)


    kik.mainloop()


M1 = Menu(M, tearoff=0)
M2 = Menu(M, tearoff=0)
M3 = Menu(M, tearoff=0)

M11 = Menu(M1, tearoff=0)

M.add_cascade(label="Файл", menu=M1)
M.add_cascade(label="Правка", menu=M2)
M.add_cascade(label="Справка", menu=M3)

M1.add_cascade(label="Сохранить", menu=M11)
M1.add_separator()
M1.add_command(label="Выход", command=on_closing)

M11.add_command(label="PDF")
M11.add_command(label="TXT")

M2.add_command(label="Настройки")

M3.add_command(label="О программе",command=dok)
M3.add_command(label="Документация")
tk.config(menu=M)

tk.mainloop()


tk.mainloop()
