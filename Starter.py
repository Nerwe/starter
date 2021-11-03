from tkinter import *
from tkinter import filedialog as fd
import os
import sys

os.system("cls")

def fill_listbox():
	listbx_file = open("data.txt","r")
	for x in listbx_file:
		listbx.insert(END,x)
	listbx_file.close()

def write_data_file():
	listbx_file = open("data.txt", "w")
	for element in data:
		listbx_file.write(element + "\n")
	listbx_file.close()

def BT_add():
	try:
		file_path = str(fd.askopenfilenames())
		file_path = file_path[2:-3]
		if file_path == "":
			return
		listbx.insert(END, file_path)
		data.append(file_path)
		write_data_file()
		lbl.configure(text = "Added", fg = 'green2')
	except:
		lbl.configure(text = "Error", fg = 'red')

def BT_delete():
	selection = listbx.curselection()[0]
	listbx.delete(selection)
	data.pop(selection)
	write_data_file()
	lbl.configure(text = "Deleted", fg = 'green2')

def BT_start():
	try:
		index = listbx.curselection()[0]
		value = str(listbx.get(index))
		value = "\"" + value + "\""
		print(value)
		os.system(value)
		lbl.configure(text = "Starting", fg = 'green2')
	except:
		lbl.configure(text = "Tuple index out of range", fg = 'red')

def BT_close():
	exit()

data = []
try:
	data_file = open("data.txt", "r")
except FileNotFoundError:
	data_file = open("data.txt", "w")
	data_file.close()
	data_file = open("data.txt", "r")
for element in data_file:
	data.append(element)
data_file.close()

win = Tk()
win.title("Prog Starter")
win.geometry('400x300')
win.resizable(width=False, height=False)
win.configure(background = 'gray25')

bt_add = Button(win, width = 15, text = "Add", command = BT_add).grid(column = 0, row = 3)
bt_start = Button(win, width = 15, text = "Start", command = BT_start).grid(column = 0, row = 4)
bt_delete = Button(win, width = 15, text = "Delete", command = BT_delete).grid(column = 0, row = 5)
bt_close = Button(win, width = 15, text = "Close", command = BT_close).grid(column = 0, row = 6)

lbl = Label(win, text = "Starter", font = ("", 15), bg = 'grey25', fg = "white")
lbl.grid(column = 0, row = 1)

listbx = Listbox(win, width = 65, height = 10, bg = "grey10", fg = "white", selectbackground = "grey20")
listbx.configure(text = fill_listbox())
listbx.grid(column=0, row=2, padx = 3)

win.mainloop()
