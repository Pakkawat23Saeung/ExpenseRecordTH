# GUIbasic2-expense.py
from this import d
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv
# ttk = theme of Tk

GUI = Tk ()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')
GUI.geometry('800x700+100+0')

#  B1 = ttk.Button(GUI,text='Hello')
#  B1.pack(ipadx=50,ipady=20) #.pack() ติดปุ่มเข้ากับ GUI หลัก
#ipadx เพิ่มความกว้างของปุ่มแกนแนว x

############MENU############
menubar = Menu(GUI)
GUI.config(menu=menubar)

##### File Menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Import csv')
filemenu.add_command(label='Export to Googlesheet')

#help function
def About():
        messagebox.showinfo('About','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูล\nสนใจบริจาคเราไหม? ขอ 1 BTC ก็พอแล้ว\nBTC Address abc')
##### Help Menu
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)


# donate fuction
def Donate():
        messagebox.showinfo('Donate','BTC Address : 46132196163516')
##### Donate Menu
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)
donatemenu.add_command(label='Donate',command=Donate)


Tab = ttk.Notebook(GUI) # เพิ่ม tab # notebook มาจาก ttk
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

expenseicon = PhotoImage(file='dollar.png').subsample(9)
listicon = PhotoImage(file='list.png').subsample(9)

Tab.add(T1,text=f'{"ค่าใช้จ่าย":^{30}}',image=expenseicon,compound='top') # compound เป็นตัวคอนโทรลรูปภาพ
Tab.add(T2,text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=listicon,compound='top')


F1 = Frame(T1)
F1.pack() #ถ้าต้องให้อยู่ตรงกลางใช้ .pack 

days = {'Mon' : 'จันทร์',
        'Tue' : 'อังคาร',
        'Wed' : 'พุธ',
        'Thu' : 'พฤหัสบดี',
        'Fri' : 'ศุกร์',
        'Sat' : 'เสาร์',
        'Sun' : 'อาทิตย์'}


def Save(event=None):        
        expense = v_expense.get() 
        number = v_count.get()
        price = v_price.get()

        if expense =='' :
                print('No Data')
                messagebox.showwarning('Error','กรุณากรอกค่าใช้จ่าย')
                return
        elif price =='' :
                messagebox.showwarning('Error','กรุณากรอกราคา')
                return
        elif number =='' :
                number = 1 

        total = float(price) * float(number) 
        try:
                total = float(price) * float(number) 
                
                # .get() คือดึงค่ามาจาก v_expense = StringVar () 
                print('รายการ: {} จำนวน :{} ราคา :{} ราคารวมทั้งหมด {}:'.format(expense,number,price,total))
                text = ('รายการ: {} จำนวน :{} \nราคา :{} ราคารวมทั้งหมด {}:'.format(expense,number,price,total))
                v_result.set(text)
               
                # clear ข้อมูลเก่า
                v_expense.set('')
                v_count.set('')
                v_price.set('')


                today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
                print(today)
                dt = datetime.now().strftime('%y-%m-%d-%H:%M:%S')
                stamp = datetime.now()
                dt = stamp.strftime('%y-%m-%d-%H:%M:%S')
                transactionid = stamp.strftime('%Y%m%d%H%M%f')
                dt = days[today] + '-' +dt

                # บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
                with open('savedata.csv','a',encoding='utf-8',newline='') as f: 
                        # with คำสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
                        # 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
                        # newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
                        fw = csv.writer(f) #สร้างฟังก์ชั่นสำหรับเขียนข้อมูล
                        data = [transactionid,dt,expense,number,price,total]
                        fw.writerow(data)

                        #ทำให้ curcor กลับไปตำแหน่งช่องกรอก E1
                E1.focus()
                update_table()
        except Exception as e:

                print('ERROR',e)
                messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่')
                v_expense.set('')
                v_count.set('')
                v_price.set('')
                
       
#  ทำให้กด enter ได้
GUI.bind('<Return>',Save) # ต้องเพิ่มใน def save(event=None) ด้วย
    
FONT1 = (None,20) # None เปลี่ยนเป็น 'Angsana New'

bg_dollar = PhotoImage(file='background.png').subsample(3) #ใส่รูปภาพพื้นหลัง

bg = Label(F1,image=bg_dollar)
bg.pack()

#-----text1-----
L = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT1).pack()
v_expense = StringVar()
# StringVar () คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable = v_expense,font=FONT1)
E1.pack()
#-----------------

#-----text2-----
L = ttk.Label(F1,text='จำนวน',font=FONT1).pack()
v_count = StringVar()
# StringVar () คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(F1,textvariable = v_count,font=FONT1) #Entry คือช่องกรอกข้อมูล ไว้กรอก input
E2.pack()
#-----------------

#-----text3-----
L = ttk.Label(F1,text='ราคา(บาท)',font=FONT1).pack()
v_price = StringVar()
# StringVar () คือตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E3 = ttk.Entry(F1,textvariable = v_price,font=FONT1) #Entry คือช่องกรอกข้อมูล ไว้กรอก input
E3.pack()
#-----------------

sv_bt = PhotoImage(file='save.png').subsample(9) #ใส่รูปภาพพื้นหลัง

B1 = ttk.Button(F1,text=f'{"Save":>15}',image=sv_bt,compound='left',command=Save)
B1.pack (ipadx=50,ipady=20,pady=20)

v_result = StringVar()
v_result.set('------ผลลัพธ์------')
result = ttk.Label(F1,textvariable=v_result,font=FONT1,foreground='green')
result.pack(pady=20)


# Tab2
def read_csv():
        with open('savedata.csv',newline='',encoding='utf-8') as f:
                fr = csv.reader(f)
                data = list(fr)
        return data

L = ttk.Label(T2,text='ตารางแสดงผลลัพธ์ทั้งหมด',font=(None,15),foreground='black')

header = ['รหัสรายการ','วัน-เวลา','รายการ','ค่าใช้จ่าย','จำนวน','รวม']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10)
resulttable.pack()

for h in header : #ทำให้หัวข้อโชว์เป็นข้อความ
        resulttable.heading(h,text=h)

headerwidth = [120,150,170,80,80,80] #ปรับขนาด table
for h,w in zip(header,headerwidth):
        resulttable.column(h,width=w)

alltransaction = {}

def UpdateCSV():
	with open('savedata.csv','w',newline='',encoding='utf-8') as f:
		fw = csv.writer(f)
		# เตรียมข้อมูลจาก alltransaction ให้กลายเป็น list
		data = list(alltransaction.values())
		fw.writerows(data) # multiple line from nested list [[],[],[]]
		print('Table was updated')



def DeleteRecord(event=None):
	check = messagebox.askyesno('Confirm?','คุณต้องการลบข้อมูลใช่หรือไม่?')
	print('YES/NO:',check)

	if check == True:
		print('delete')
		select = resulttable.selection()
		#print(select)
		data = resulttable.item(select)
		data = data['values']
		transactionid = data[0]
		#print(transactionid)
		#print(type(transactionid))
		del alltransaction[str(transactionid)] # delete data in dict
		#print(alltransaction)
		UpdateCSV()
		update_table()
	else:
		print('cancel')

BDelete = ttk.Button(T2,text='Delete',command=DeleteRecord)
BDelete.place(x=50,y=550)

resulttable.bind('<Delete>',DeleteRecord)

def update_table():
	resulttable.delete(*resulttable.get_children())
	# for c in resulttable.get_children():
	# 	resulttable.delete(c)
	try:
		data = read_csv()
		for d in data:
			#creat transaction data
			alltransaction[d[0]] = d # d[0] = transactionid
			resulttable.insert('',0,value=d)
		print(alltransaction)
	except Exception as e:
		print('No File')
		print('ERROR:',e)


update_table()
print('GET CHILD:',resulttable.get_children())
GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()