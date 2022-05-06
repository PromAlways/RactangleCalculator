#RactangleCalculator.py

from tkinter import * 
from tkinter import ttk ,messagebox

rac_cal = Tk ()
rac_cal.title('Area Calculator')
rac_cal.geometry('350x350')
rac_cal.resizable(0,0)

W = Label (rac_cal,text='Enter Width',font=(None,15))
W.pack()
W_quantity = StringVar() #ใช้เก็บข้อความเมื่อพิมเสร็จแล้ว
W1 = ttk.Entry(rac_cal,textvariable=W_quantity,font=(None,20))
W1.pack()

H = Label (rac_cal,text='Enter Height',font=(None,15))
H.pack()
H_quantity = StringVar() #ใช้เก็บข้อความเมื่อพิมเสร็จแล้ว
H1 = ttk.Entry(rac_cal,textvariable=H_quantity,font=(None,20))
H1.pack()

def Cal():
        Wget = float(W_quantity.get())
        Hget = float(H_quantity.get())
        calc = Wget * Hget #การคำนวน
        messagebox.showinfo('Area total','Area is {} '.format(calc) )
      

B = ttk.Button(rac_cal,text='Calculator',command=Cal)
B.pack(ipadx=15,ipady=10,expand=True,side='right')

exit_button = ttk.Button(rac_cal,text='Close',command=rac_cal.quit)
exit_button.pack(ipadx=15,ipady=10,expand=True,side='left')

rac_cal.mainloop() #ให้โปรแกรมรันตลอดเวลา








