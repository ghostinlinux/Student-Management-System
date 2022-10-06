from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry("1200x550")
root.title("STUDENT DATABASE")
# Creating Tab control below
tabctrl = ttk.Notebook(root)
tab1 = ttk.Frame(tabctrl)
tabctrl.add(tab1, text='New Student')
tab2 = ttk.Frame(tabctrl)
tabctrl.add(tab2, text='Display')
tab3 = ttk.Frame(tabctrl)
tabctrl.add(tab3, text='Course Creation')
tab4 = ttk.Frame(tabctrl)
tabctrl.add(tab4, text='Display Courses')
tab5 = ttk.Frame(tabctrl)
tabctrl.add(tab5, text='Course Allocation')
tabctrl.pack(expand=1, fill="both")
# Entering content in tab1
ttk.Label(tab1, text='Enter Your Name :').place(x=80, y=0)
box_1 = StringVar()
e1 = ttk.Entry(tab1, width=75, textvariable=box_1)
e1.place(x=500, y=0)

ttk.Label(tab1, text='Enter Your Roll No. :').place(x=80, y=40)
box_2 = StringVar()
e2 = ttk.Entry(tab1, width=75, textvariable=box_2)
e2.place(x=500, y=40)

# Radiobutton code below
_m = 'Male'
_f = 'Female'
ttk.Label(tab1, text='Choose your Gender :').place(x=80, y=80)
v = StringVar()
ttk.Radiobutton(tab1, text='Male', variable=v, value=_m).place(x=500, y=80)
ttk.Radiobutton(tab1, text='Female', variable=v, value=_f).place(x=895, y=80)
ttk.Label(tab1, text='Choose your Gender :').place(x=80, y=80)

ttk.Label(tab1, text='Address for Correspondence :').place(x=80, y=120)
box_3 = StringVar()
e3 = ttk.Entry(tab1, width=75, textvariable=box_3)
e3.place(x=500, y=120)

ttk.Label(tab1, text='Phone No. :').place(x=80, y=160)
box_4 = StringVar()
e4 = ttk.Entry(tab1, width=75, textvariable=box_4)
e4.place(x=500, y=160)

# Option menu code below
ttk.Label(tab1, text='Your Batch :').place(x=80, y=200)
box_5 = StringVar()
optlist = ['2016', '2017', '2018', '2019', '2020']
box_5.set(optlist[0])
opt = OptionMenu(tab1, box_5, *optlist)
opt.place(x=792, y=200)

# Checkbox code below
ttk.Label(tab1, text='Hostel[Y/N] :').place(x=80, y=240)
v1 = BooleanVar()
c = ttk.Checkbutton(tab1, text='Click if you need Hostel Facility', variable=v1)
c.place(x=770, y=240)

# Tree view widget below
columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
tree = ttk.Treeview(tab2, columns=columns, height=25)
# Heading
tree.heading('#0', text='S No.')
tree.heading('#1', text='Roll No.')
tree.heading('#2', text='Name')
tree.heading('#3', text='Gender')
tree.heading('#4', text='Address')
tree.heading('#5', text='PhoneNo')
tree.heading('#6', text='Batch')
tree.heading('#7', text='Hostel')
# Columns
tree.column('#0', stretch=NO, width=0)
tree.column('#1', stretch=NO)
tree.column('#2', stretch=NO)
tree.column('#3', stretch=NO)
tree.column('#4', stretch=NO)
tree.column('#5', stretch=NO)
tree.column('#6', stretch=NO)
tree.column('#7', stretch=NO, width=65)

tree.grid(row=2, columnspan=2, sticky='nsew')
treeview = tree


# Defining entry for save button
def insert_data():
    i = 0
    treeview.insert('', index='end',
                    values=(box_2.get(), box_1.get(), v.get(), box_3.get(), box_4.get(), box_5.get(), v1.get()))

    i = i + 1

# Function for json file


def writeToJSONFile(path, fileName, data):
    json.dump(data, path)


path = './'


# Defining function to store data in json file
def check():
    a = e1.get()
    b = e2.get()
    c1 = v.get()
    d = e3.get()
    e = e4.get()
    f = box_5.get()
    g = v1.get()
    print(a)
    print(b)
    print(c1)
    print(d)
    print(e)
    print(f)
    print(g)

    data = {}
    data['Name'] = a
    data['RollNo'] = b
    data['Gender'] = c1
    data['Address'] = d
    data['PhoneNo'] = e
    data['Batch'] = f
    data['Hostel'] = g
    files = [('JSON File', '*.json')]
    fileName = 'Students'
    filepos = asksaveasfile(filetypes=files, defaultextension=json, initialfile='Students')
    writeToJSONFile(filepos, fileName, data)
# Save and Clear Buttons below


def clicked():
    messagebox.showinfo('Save', 'Your record have been saved!')


def delete():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    v.set(0)
    v1.set(0)
    
#######################new###    
def multi_func():
    clicked()
    check()
    insert_data()


btn1 = ttk.Button(tab1, text='Save', width=15, command=multi_func)
btn1.place(x=300, y=320)
ttk.Button(tab1, text='Clear', width=15, command=delete).place(x=450, y=320)

# Entering content in tab3
ttk.Label(tab3, text='Course ID :').place(x=200, y=100)
box_6 = StringVar()
e6 = ttk.Entry(tab3, width=75, textvariable=box_6)
e6.place(x=500, y=100)

ttk.Label(tab3, text='Course Name :').place(x=200, y=200)
box_7 = StringVar()
e7 = ttk.Entry(tab3, width=75, textvariable=box_7)
e7.place(x=500, y=200)

# Tree view for tab4 below
columns = ('#1', '#2')
tree1 = ttk.Treeview(tab4, columns=columns, height=25)
# Heading
tree1.heading('#0', text='S No.')
tree1.heading('#1', text='Course ID')
tree1.heading('#2', text='Course Name')
# Columns
tree1.column('#0', stretch=NO, width=0)
tree1.column('#1', stretch=NO)
tree1.column('#2', stretch=NO)

tree1.grid(row=2, columnspan=2, sticky='nsew')
treeview1 = tree1

# Storing json file in tab3


def writeToJSONFile1(path1, fileName1, data1):
    json.dump(data1, path1)


path1 = './'


def check1():
    m = e6.get()
    n = e7.get()
    print(m)
    print(n)
    data1 = {}
    data1['Course Id'] = m
    data1['Course Name'] = n
    files = [('JSON File', '*.json')]
    fileName1 = 'Course'
    filepos = asksaveasfile(filetypes=files, defaultextension=json, initialfile='Course')
    writeToJSONFile1(filepos, fileName1, data1)

# Functions for Save and Clear buttons


def insert_data1():
    i = 0
    treeview1.insert('', index='end',
                       values=(box_6.get(), box_7.get()))

    i = i + 1


def delete1():
    e6.delete(0, 'end')
    e7.delete(0, 'end')


def multi_func1():
    insert_data1()
    check1()


# Save and Clear buttons below
ttk.Button(tab3, text='Save', width=15, command=multi_func1).place(x=400, y=320)
ttk.Button(tab3, text='Clear', width=15, command=delete1).place(x=550, y=320)

# Entering content in tab5
ttk.Label(tab5, text='Student Roll No :').place(x=200, y=100)
box_8 = StringVar()
e8 = ttk.Entry(tab5, width=75, textvariable=box_8)
e8.place(x=500, y=100)

ttk.Label(tab5, text='Course Name :').place(x=200, y=200)
box_9 = StringVar()
e9 = ttk.Combobox(tab5, width=75, textvariable=box_9, values=['Programming in C', 'Problem Solving With Python',
                                 'Object Oriented Programming in Linux', 'Introduction to Linux',
                                 'Database Management System', 'Computer Networks', 'Advanced Web Technologies'])
e9.place(x=500, y=200)


# Storing json file in tab5
def writeToJSONFile2(path2, fileName2, data2):
    json.dump(data2, path2)


path2 = './'


def check2():
    x = e8.get()
    y = box_9.get()
    print(x)
    print(y)
    data2 = {}
    data2['RollNo'] = x
    data2['Course'] = y
    files = [('JSON File', '*.json')]
    fileName2 = 'Allocation'
    filepos = asksaveasfile(filetypes=files, defaultextension=json, initialfile='Allocation')
    writeToJSONFile(filepos, fileName2, data2)


# Save and Clear buttons below
ttk.Button(tab5, text='Allocate', width=15, command=check2).place(x=470, y=360)

root.mainloop()