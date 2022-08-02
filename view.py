from tkinter import *
import tkinter.messagebox as messagebox
from controller import Controller


controller = Controller()

# ------------------------------------------
def add():
    id = e_id.get()
    name = e_name.get()
    family = e_family.get()
    average = e_average.get()

    if id == '' or name == '' or family == '' or average == '':
        messagebox.showinfo("Add Status","All fields are requierd!")
    else:
        controller.add(id, name, family, average)
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_family.delete(0, 'end')
        e_average.delete(0, 'end')
        rows = controller.select()
        show(rows)
        messagebox.showinfo("Add Status", "Added Successfully")


# ------------------------------------------
def delete():
    if(e_id.get() == ''):
        messagebox.showinfo("Delete Status", "ID is empty")
    else:
        controller.delete(e_id.get())
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_family.delete(0, 'end')
        e_average.delete(0, 'end')
        rows = controller.select()
        show(rows)
        messagebox.showinfo("Delete Status", "Deleted Successfully")


# ------------------------------------------
def update():
    id = e_id.get()
    name = e_name.get()
    family = e_family.get()
    average = e_average.get()
    if (id == '' or name == '' or family == '' or average == ''):
        messagebox.showinfo("Update Status","All fields are requierd!")
    else:
        controller.update(id, name, family, average)
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_family.delete(0, 'end')
        e_average.delete(0, 'end')
        rows = controller.select()
        show(rows)
        messagebox.showinfo("Update Status", "Updated Successfully")


# ------------------------------------------
def select():
    rows = controller.select_by_condition((e_id.get(), e_name.get(), e_family.get(), e_average.get()))
    show(rows)


# --------------------------view-----------------------


def show(rows):
    reset_frame()

    new_root = frame

    for i, column in enumerate(["ID", "Name", "Family", "Average"]):
        temp_label = Label(new_root, text=column, width=15, height=2, borderwidth=1, fg="black", relief="solid")
        temp_label.grid(row=0, column=i)
    print(rows)
    for i, row in enumerate(rows):
        temp_label = Label(new_root, text=row[0], width=15, height=2, borderwidth=1, fg="black", relief="solid")
        temp_label1 = Label(new_root, text=row[1], width=15, height=2, borderwidth=1, fg="black", relief="solid")
        temp_label2 = Label(new_root, text=row[2], width=15, height=2, borderwidth=1, fg="black", relief="solid")
        temp_label3 = Label(new_root, text=row[3], width=15, height=2, borderwidth=1, fg="black", relief="solid")
        temp_label.grid(row=i + 1, column=0)
        temp_label1.grid(row=i + 1, column=1)
        temp_label2.grid(row=i + 1, column=2)
        temp_label3.grid(row=i + 1, column=3)


#  -------------------------------------------------
def reset_frame():
    global frame
    for widgets in frame.winfo_children():
        widgets.destroy()

#  -------------------------------------------------


root = Tk()
root.geometry('500x400')
root.title('Student')
root.configure(background='black')


id = Label(root, text='ID', borderwidth=1, relief='solid')
id.place(x=20, y=30)

name = Label(root, text='Name', borderwidth=1, relief='solid')
name.place(x=20,y=60)

family = Label(root, text='Family', borderwidth=1, relief='solid')
family.place(x=20,y=90)

average = Label(root, text='Average', borderwidth=1, relief='solid')
average.place(x=20 ,y=120)

e_id = Entry()
e_id.place(x=100,y=30)

e_name = Entry()
e_name.place(x=100,y=60)

e_family= Entry()
e_family.place(x=100,y=90)

e_average = Entry()
e_average.place(x=100,y=120)

add = Button(root, text='Add', bg='blue', command = add)
add.place(x=60,y=160)

update = Button(root, text='Update', bg='yellow', command = update)
update.place(x=100,y=160)

delete = Button(root, text='Delete', bg='red', command = delete)
delete.place(x=160,y=160)

select = Button(root, text='Select', bg='green', command=select)
select.place(x=210,y=160)

frame = Frame(root, relief="solid", bg='black', width=500, height=500)
frame.place(x=20, y=200)

root.mainloop()











