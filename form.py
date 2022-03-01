from tkinter import *
import tkinter.messagebox

def validate():
    name= entry_3.get()
    company= c.get()
    idnumber=entry_2.get()
    Tell=entry_4.get()
    # programming= var2.get()
    gender= var.get()
    if (name=="" or idnumber=="" or company== 'Select company'or gender == 0 or Tell==""):
        tkinter.messagebox.showinfo('Invalid Message Alert',"Fields cannot be left empty!")

    else:
        import qrcode
        img = qrcode.make(name+"/"+idnumber + "/" + Tell + "/" + company + "/"+ gender)
        type(img)  # qrcode.image.pil.PilImage
        img.save(idnumber)
        #entry_2.set_text("")

        tkinter.messagebox.showinfo('Success Message',"Successfully registered!")
        clear_text()
        

 
def clear_text():
   entry_2.delete(0, END)
   entry_3.delete(0, END)
   entry_4.delete(0, END)
   var.set(None)
   c.set('Select company') 
root = Tk()
root.geometry('500x500')
root.title("SanTech QR Code Generator")


label_0 = Label(root, text="Staff Card QR Code Generation",width=40,font=("bold", 20))
label_0.place(x=0,y=53)

label_2 = Label(root, text="ID NUmber",width=20,font=("bold", 10))
label_2.place(x=68,y=160)


entry_2 = Entry(root)
entry_2.place(x=240,y=160)


label_2 = Label(root, text="Tell",width=20,font=("bold", 10))
label_2.place(x=50,y=200)

entry_4 = Entry(root)
entry_4.place(x=240,y=200)

label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
label_1.place(x=68,y=130)

entry_3 = Entry(root)
entry_3.place(x=240,y=130)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=55,y=230)
var = StringVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Company",width=20,font=("bold", 10))
label_4.place(x=55,y=280)

list1 = ['company1 ','Company2','Company3','Company4','Company5','Company6'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Select company') 
droplist.place(x=240,y=280)
#var1 = IntVar()
# Checkbutton(root, text="C++", variable=var1).place(x=235,y=330)
# var2 = IntVar()
# Checkbutton(root, text="Python", variable=var2).place(x=290,y=330)

Button(root, text='Submit',width=20,bg='green',fg='white', command = validate).place(x=180,y=380)

root.mainloop()
