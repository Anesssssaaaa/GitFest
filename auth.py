from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import os

dirname=os.path.dirname(__file__)
os.chdir(dirname)
 
      
def on_login():
    entry_user = user_combobox.get()
    entry_password = password_entry.get() 
     
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM tab_2 WHERE username=? AND password=?", (entry_user, entry_password))
    base_user = cursor.fetchone()
    connection.commit()
    connection.close()
    # print(base_user)
    
    if base_user:
        if entry_user=="Администратор":
            tk.destroy()
            import main
        else:
            tk.destroy()
            import main_user
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")



tk = Tk()
tk.title("Авторизация")
tk.geometry("400x200")
tk.resizable(False, False)
    


connection = sqlite3.connect('base.db')
cursor = connection.cursor()
cursor.execute("SELECT username FROM tab_2")
users =  cursor.fetchall()
connection.commit()
connection.close()  
    

Label(tk, text="Пользователь:").place(x=50, y=40)

user_combobox = ttk.Combobox(tk, values=users, width=25)
user_combobox.place(x=50, y=65)

if users:
    user_combobox.current(0)
    
Label(tk, text="Пароль:").place(x=50, y=100)
password_entry = Entry(tk, show="*", width=28) 
password_entry.place(x=50, y=125)
    
# Кнопки
login_btn = Button(tk, text="Войти", width=10, command=on_login)
login_btn.place(x=100, y=160)
    
cancel_btn = Button(tk, text="Отмена", width=10, command=tk.destroy)
cancel_btn.place(x=200, y=160)
    

password_entry.focus_set()
    

password_entry.bind('<Return>', lambda event: on_login())
    
tk.mainloop()



