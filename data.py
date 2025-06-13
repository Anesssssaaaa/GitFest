from tkinter import END, DISABLED, NORMAL
import datetime

def save_data(tree, log_file, E_t, E_m, E_n, E_f, L_id, B_del, B_edit, B_Enter, connection, cursor):
    
    t=E_t.get()
    m=E_m.get()
    n=E_n.get()
    f=E_f.get()
  
      
    cursor.execute("UPDATE tab_3 SET №ТС=?, МАРКА=?, НАЗВАНИЕ=?, ФИО=? WHERE id=?", (t, m, n, f, id))
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_3")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d) 
        
    E_t.delete(0, END)
    E_m.delete(0, END)
    E_n.delete(0, END)
    E_f.delete(0, END)

    B_del.config(state=NORMAL)
    B_edit.config(state=NORMAL)
    B_Enter.config(text="Ввод", command=lambda:  add_data(tree, E_t,E_m,E_n,E_f, log_file, connection, cursor))
    L_id.config(text="IID:")

    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} изменена\n")

def del_data(tree, log_file, connection, cursor):
    data = tree.item(tree.selection())
    data_ID=data["values"][0]
    cursor.execute(f"DELETE FROM tab_3 WHERE id={data_ID}")
    connection.commit()

    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_3")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)
    
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {data_ID} удалена\n")
    

def edit_data(tree, log_file, E_t, E_m, E_n, E_f, L_id, B_del, B_edit, B_Enter, connection, cursor):
    global id
    iid = tree.selection()
    
    
    id = tree.item(iid)["values"][0]
    t = tree.item(iid)["values"][1]
    m = tree.item(iid)["values"][2]
    n = tree.item(iid)["values"][3]
    f = tree.item(iid)["values"][4]

    L_id.config(text=id)

    E_t.insert(0,t)
    E_m.insert(0,m)
    E_n.insert(0,n)
    E_f.insert(0,f)

    B_del.config(state=DISABLED)
    B_edit.config(state=DISABLED)
    B_Enter.config(text="Сохранить", command=lambda: save_data(tree, log_file, E_t,E_m,E_n,E_f, L_id, B_del, B_edit, B_Enter, connection, cursor))

def add_data(tree, E_t, E_m, E_n, E_f, log_file, connection, cursor):
    

    t = E_t.get()
    m = E_m.get()
    n = E_n.get()
    f = E_f.get()

        
    
    
    cursor.execute("INSERT INTO tab_3 (№ТС,МАРКА,НАЗВАНИЕ,ФИО) VALUES (?, ?, ?, ?)", ( t, m, n, f))
    connection.commit()
    for item in tree.get_children():
        tree.delete(item)
    cursor.execute("SELECT * FROM tab_3")
    pipls = cursor.fetchall()
    connection.commit()    
    for d in pipls:
        tree.insert('', END, values=d)    
    
    
    now=datetime.datetime.now()
    name = now.strftime("%d.%m.%Y_%H.%M.%S")
    log_file.write(f"{name} Запись {id} добавлена\n")
        
    E_t.delete(0, END)
    E_m.delete(0, END)
    E_n.delete(0, END)
    E_f.delete(0, END)
