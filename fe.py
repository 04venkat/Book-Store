from tkinter import *
import be

win = Tk()
win.wm_title("BookStore")

def return_row(event):
    try:
        global sel_tup
        index = li1.curselection()[0]
        sel_tup = li1.get(index)

        title.delete(0, END)
        title.insert(END, sel_tup[1])

        author.delete(0, END)
        author.insert(END, sel_tup[2])

        year.delete(0, END)
        year.insert(END, sel_tup[3])
        
        isbn.delete(0, END)
        isbn.insert(END, sel_tup[4])
    except IndexError:
        pass

def be_view_all():
    li1.delete(0, END)
    for row in be.view_all():
        li1.insert(END, row)
        
def be_search():
    li1.delete(0, END)
    for row in be.search(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get()):
        li1.insert(END, row)
    title.delete(0, END)
    author.delete(0, END)
    year.delete(0, END)
    isbn.delete(0, END)      

def be_delete():
    be.delete(sel_tup[0])
    li1.delete(0, END)
    li1.insert(END, "Book Details Deleted Successfully!")
    title.delete(0, END)
    author.delete(0, END)
    year.delete(0, END)
    isbn.delete(0, END)


def be_add_entry():
    li1.delete(0, END)
    be.add_entry(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
    li1.insert(END, "Book Details Added Successfully!")
    title.delete(0, END)
    author.delete(0, END)
    year.delete(0, END)
    isbn.delete(0, END)

def be_update():
    be.update(sel_tup[0], title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
    li1.delete(0, END)
    li1.insert(END, "Book Details Updated Successfully!")
    title.delete(0, END)
    author.delete(0, END)
    year.delete(0, END)
    isbn.delete(0, END)

def be_exit():
    win.destroy()    

l1 = Label(win, text="Title")
l1.grid(row= 0, column=0)

title_entry = StringVar()
title = Entry(win, textvariable= title_entry)
title.grid(row= 0, column=1)

l2 = Label(win, text="Author")
l2.grid(row= 0, column=2)

author_entry = StringVar()
author = Entry(win, textvariable= author_entry)
author.grid(row= 0, column=3)

l3 = Label(win, text="Year")
l3.grid(row= 1, column=0)

year_entry = StringVar()
year = Entry(win, textvariable= year_entry)
year.grid(row= 1, column=1)

l4 = Label(win, text="ISBN")
l4.grid(row= 1, column=2)

isbn_entry = StringVar()
isbn = Entry(win, textvariable= isbn_entry)
isbn.grid(row= 1, column=3)

li1 = Listbox(win, height=20, width=75)
li1.grid(row= 2, column=0, columnspan= 4)

sc = Scrollbar(win)
sc.grid(row=2, column=4)

li1.configure(yscrollcommand=sc.set)
sc.configure(command=li1.yview)
li1.bind("<<ListboxSelect>>", return_row)

b1 = Button(win, text="View All", width=10, command=be_view_all)
b1.grid(row=3, column=0)

b1 = Button(win, text="Search", width=10, command=be_search)
b1.grid(row=3, column=2)

b1 = Button(win, text="Delete", width=10, command=be_delete)
b1.grid(row=3, column=4)

b1 = Button(win, text="Add Entry", width=10, command=be_add_entry)
b1.grid(row=4, column=0)

b1 = Button(win, text="Update", width=10, command=be_update)
b1.grid(row=4, column=2)

b1 = Button(win, text="Exit", width=10, command=be_exit)
b1.grid(row=4, column=4)

win.mainloop()