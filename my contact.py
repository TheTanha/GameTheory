from pathlib import Path
import json
from tkinter import *
from tkinter import messagebox

window = Tk()

window.title('دفترچه تلفن')
window.geometry("950x200")
window.configure(bg="gray")


L_row = Label(text='ردیف', fg="yellow",
              bg="black", font=("B Yekan", 12), width=5)
L_row.grid(row=0, column=5, padx=10, pady=10)
E_row = Entry(font=("B Yekan", 12), width=5)
E_row.grid(row=1, column=5, padx=10)

L_name = Label(text="نام و نام خانوادگی", bg="black", fg="yellow",
               font=("B Yekan", 12), width=20)
L_name.grid(row=0, column=4)
E_name = Entry(font=("B Yekan", 12))
E_name.grid(row=1, column=4, padx=10)

L_mobile = Label(text="شماره همراه", bg="black", fg="yellow",
                 font=("B Yekan", 12), width=20)
L_mobile.grid(row=0, column=3)
E_mobile = Entry(font=("B Yekan", 12))
E_mobile.grid(row=1, column=3, padx=10)

L_home = Label(text="شماره منزل", bg="black", fg="yellow",
               font=("B Yekan", 12), width=20)
L_home.grid(row=0, column=2)
E_home = Entry(font=("B Yekan", 12))
E_home.grid(row=1, column=2, padx=10)

L_mail = Label(text="پست الکترونیکی", bg="black",
               fg="yellow", font=("B Yekan", 12), width=20)
L_mail.grid(row=0, column=1)
E_mail = Entry(font=("B Yekan", 12))
E_mail.grid(row=1, column=1, padx=10)


L_last = Label(text='آخرین نفر     >>>', fg="yellow",
               bg="black", font=("B Yekan", 12), width=17)
L_last.grid(row=2, column=4, padx=10, pady=10)
E_last = Entry(font=("B Yekan", 12), width=5)
E_last.grid(row=2, column=5, padx=10)

iut = Label(text="1", bg="gray", fg='gray', width=1)
iut.grid(row=0, column=0, padx=10)
####################################################

path_name = Path("name.json")
if path_name.exists():
    with open("name.json", "r") as file:
        dict_name = json.load(file)
else:
    dict_name = {}

path_mobile = Path("mobile.json")
if path_mobile.exists():
    with open("mobile.json", "r") as file:
        dict_mobile = json.load(file)
else:
    dict_mobile = {}

path_home = Path("home.json")
if path_home.exists():
    with open("home.json", "r") as file:
        dict_home = json.load(file)
else:
    dict_home = {}

path_mail = Path("mail.json")
if path_mail.exists():
    with open("mail.json", "r") as file:
        dict_mail = json.load(file)
else:
    dict_mail = {}

####################################################

E_last.delete(0, END)
E_last.insert(0, len(dict_name))


def register(event):

    row = E_row.get()
    E_row.delete(0, END)

    name = E_name.get()
    E_name.delete(0, END)

    mobile = E_mobile.get()
    E_mobile.delete(0, END)

    home = E_home.get()
    E_home.delete(0, END)

    mail = E_mail.get()
    E_mail.delete(0, END)

    dict_name[row] = name

    import json
    with open("name.json", "w") as file:
        json.dump(dict_name, file, indent=4)

    dict_mobile[row] = mobile

    with open("mobile.json", "w") as file:
        json.dump(dict_mobile, file, indent=4)

    dict_home[row] = home

    with open("home.json", "w") as file:
        json.dump(dict_home, file, indent=4)

    dict_mail[row] = mail

    with open("mail.json", "w") as file:
        json.dump(dict_mail, file, indent=4)

    E_last.delete(0, END)
    E_last.insert(0, len(dict_name))


def search(event):

    row = E_row.get()
    name = E_name.get()
    mobile = E_mobile.get()
    home = E_home.get()
    mail = E_mail.get()

    for i in dict_name:
        if dict_name[i] == name:
            row = i

    for i in dict_mobile:
        if dict_mobile[i] == mobile:
            row = i

    for i in dict_home:
        if dict_home[i] == home:
            row = i

    for i in dict_mail:
        if dict_mail[i] == mail:
            row = i

    if row in dict_name:

        E_row.delete(0, END)
        E_row.insert(0, row)

        E_name.delete(0, END)
        E_name.insert(0, dict_name[row])

        E_mobile.delete(0, END)
        E_mobile.insert(0, dict_mobile[row])

        E_home.delete(0, END)
        E_home.insert(0, dict_home[row])

        E_mail.delete(0, END)
        E_mail.insert(0, dict_mail[row])
    else:
        E_name.delete(0, END)
        E_name.insert(0, "پیدا نشد")
        E_mobile.delete(0, END)
        E_mobile.insert(0, "پیدا نشد")
        E_home.delete(0, END)
        E_home.insert(0, "پیدا نشد")
        E_mail.delete(0, END)
        E_mail.insert(0, "پیدا نشد")
        messagebox.showwarning(message="Not found")


def delete(event):
    E_row.delete(0, END)
    E_name.delete(0, END)
    E_mobile.delete(0, END)
    E_home.delete(0, END)
    E_mail.delete(0, END)


B_register = Button(text="ثبت", font=("B Yekan", 12),
                    bg="yellow", fg="black", padx=70, pady=1)
B_register.grid(row=2, column=1, padx=10, pady=15)
B_register.bind("<Button-1>", register)

B_search = Button(text="جستو", bg="yellow",
                  font=("B Yekan", 12), padx=70, pady=1)
B_search.grid(row=2, column=2, padx=10, pady=15)
B_search.bind("<Button-1>", search)


B_delete = Button(text="پاک کردن", fg="black", bg="red",
                  font=("B Yekan", 12), padx=56, pady=1)
B_delete.grid(row=2, column=3, padx=10, pady=15)
B_delete.bind("<Button-1>", delete)


window.mainloop()
