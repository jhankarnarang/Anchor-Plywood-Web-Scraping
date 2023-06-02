import tkinter as tk
from tkinter import ttk
import mysql.connector

def show():
	mysqldb = mysql.connector.connect(host="localhost", user="root", password="Shub@8877240694", database="college")
	mycursor = mysqldb.cursor()
	mycursor.execute("SELECT emp_id,emp_name,emp_email,emp_mob FROM student")
	records = mycursor.fetchall()
	print(records)

	for i, (id,stname, course,fee) in enumerate(records, start=1):
		Label.insert("", "end", values=(id, stname, course, fee))
		mysqldb.close()




root = tk.Tk()
root.title("Student Records")
Label = tk.Label(root, text="Student Records", font=("Arial",30)).grid(row=0, columnspan=3)

cols = ('id', 'stname', 'course','fee')
Label = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    Label.heading(col, text=col)    
    Label.grid(row=1, column=0, columnspan=2)
closeButton = tk.Button(root, text="Close", width=15, command=exit).grid(row=4, column=1)
show()
root.mainloop()