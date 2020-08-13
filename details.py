from tkinter import *
import mysql.connector

root =Tk()
root.title("Student Details")
root.geometry("400x600")

f_name_result = Label(root)
l_name_result = Label(root)
roll_result = Label(root)

def results():
	f_name_got=  f_name.get()
	l_name_got = l_name.get()
	roll_got = roll.get()

	mydb = mysql.connector.connect(host = "localhost",user="root",passwd ="password",database="college")
	mycursor = mydb.cursor()

	insert_stmt = "INSERT INTO student_details(roll_no,first_name,last_name) VALUES(%s,%s,%s)"

	data = (roll_got,f_name_got,l_name_got)

	mycursor.execute(insert_stmt,data)

	mydb.commit()
	mydb.close()

def get_fname():
	global f_name_result
	f_name_result.destroy()
	first = (f_name_get).get()
	mydb = mysql.connector.connect(host = "localhost",user="root",passwd ="password",database="college")
	mycursor = mydb.cursor()

	get_stmt = "SELECT * FROM student_details WHERE first_name=%s"

	mycursor.execute(get_stmt,(first,))

	result = mycursor.fetchall()

	print_records=""
	for  record in result:
		   print_records += str(record[0]) + " "+"\t" + str(record[1])+" "+"\t"+ str(record[2])+"\n"


	some_text = "RollNO"+" "+"\t" + "FirstName"+"  "+ "LastName"
	text_res = Label(root,text=some_text)
	text_res.grid(row=7,column=0,columnspan=2)

	f_name_result = Label(root,text=print_records)
	f_name_result.grid(row=8,column=0,columnspan=2)

	mydb.commit()
	mydb.close()


def get_lname():
	global l_name_result
	l_name_result.destroy()
	last = (l_name_get).get()
	mydb = mysql.connector.connect(host = "localhost",user="root",passwd ="password",database="college")
	mycursor = mydb.cursor()

	get_stmt = "SELECT * FROM student_details WHERE last_name=%s"

	mycursor.execute(get_stmt,(last,))

	result = mycursor.fetchall()

	print_records=""
	for  record in result:
		   print_records += str(record[0]) + " "+"\t" + str(record[1])+" "+"\t"+ str(record[2])+"\n"

	some_text = "RollNO"+" "+"\t" + "FirstName"+"  "+ "LastName"
	text_res = Label(root,text=some_text)
	text_res.grid(row=10,column=0,columnspan=2)

	l_name_result = Label(root,text=print_records)
	l_name_result.grid(row=11,column=0,columnspan=2)

	mydb.commit()
	mydb.close()

def get_roll():
	global roll_result
	roll_result.destroy()
	Roll = (roll_get).get()
	mydb = mysql.connector.connect(host = "localhost",user="root",passwd ="password",database="college")
	mycursor = mydb.cursor()

	get_stmt = "SELECT * FROM student_details WHERE roll_no=%s"

	mycursor.execute(get_stmt,(Roll,))

	result = mycursor.fetchall()

	print_records=""
	for  record in result:
		   print_records += str(record[0]) + " "+"\t" + str(record[1])+" "+"\t"+ str(record[2])+"\n"

	some_text = "RollNO"+" "+"\t" + "FirstName"+"  "+ "LastName"
	text_res = Label(root,text=some_text)
	text_res.grid(row=13,column=0,columnspan=2)

	roll_result = Label(root,text=print_records)
	roll_result.grid(row=14,column=0,columnspan=2)

	mydb.commit()
	mydb.close()
	 



mylabel = Label(root,text ="Enter Details",font=("Helvetica",20))
mylabel.grid(row =0 ,column=0,columnspan=2,pady=10,padx=10) 

f_name_label = Label(root,text ="First Name",font=("Helvetica"))
f_name_label.grid(row=1,column =0,pady=5)

l_name_label = Label(root,text ="Last Name",font=("Helvetica"))
l_name_label.grid(row=2,column =0,pady=5)

roll_label = Label(root,text ="Roll No",font=("Helvetica"))
roll_label.grid(row=3,column =0,pady=5)

f_name = Entry(root,width=20)
f_name.grid(row=1,column =1,padx=20)

l_name = Entry(root,width=20)
l_name.grid(row=2,column =1,pady=5)

roll = Entry(root,width=20)
roll.grid(row=3,column =1,pady=5)

enter_button = Button(root,text="Enter",command = results)
enter_button.grid(row =4 ,column=0,columnspan=2,pady=10,padx=10) 


# Get Details
myget = Label(root,text ="Get Details",font=("Helvetica",20))
myget.grid(row =5 ,column=0,columnspan=2,pady=10,padx=10) 

#first Name
f_get_label = Label(root,text ="First Name",font=("Helvetica"))
f_get_label.grid(row=6,column =0,pady=5)
f_name_get = Entry(root,width=20)
f_name_get.grid(row=6,column =1,padx=20)
enter_fname = Button(root,text="Enter",command=get_fname)
enter_fname.grid(row =6 ,column=2,columnspan=2,pady=10,padx=10) 

l_get_label = Label(root,text ="Last Name",font=("Helvetica"))
l_get_label.grid(row=9,column =0,pady=5)
l_name_get = Entry(root,width=20)
l_name_get.grid(row=9,column =1,padx=20)
enter_lname = Button(root,text="Enter",command=get_lname)
enter_lname.grid(row =9 ,column=2,columnspan=2,pady=10,padx=10) 

roll_get_label = Label(root,text ="Roll No",font=("Helvetica"))
roll_get_label.grid(row=12,column =0,pady=5)
roll_get = Entry(root,width=20)
roll_get.grid(row=12,column =1,padx=20)
enter_roll = Button(root,text="Enter",command=get_roll)
enter_roll.grid(row =12 ,column=2,columnspan=2,pady=10,padx=10) 


root.mainloop()

