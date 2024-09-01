from tkinter import *
import pyqrcode
import png 
from tkinter import filedialog
from PIL import Image,ImageTk

root=Tk()
root.title("QR CODE CREATER")
root.iconbitmap('E:\MY projects\python\QrTkinter')
root.geometry('450x500')
root.config(bg="light blue")


def create_code():
    
    #File Dialog
    input_path= filedialog.asksaveasfilename(title="Save Image",filetypes=(("PNG FILE",".png"),("All Files","*,*")))  
    
    if input_path:
        if input_path.endswith(".png"):
            #create qr code from entry box
            get_code =pyqrcode.create(my_entry.get())
            #save as png
            get_code.png(input_path,scale=5)
        else:
            #Add that .png to the end of the file name
            input_path=f'{input_path}.png'
            #create qr code from entry box
            get_code =pyqrcode.create(my_entry.get())
            #save as png
            get_code.png(input_path,scale=5)  

        #Put qr code in screen
        global get_image
        get_image=ImageTk.PhotoImage(Image.open(input_path))
        #Add image to label
        my_label.config(image=get_image)

        #Delete entry box
        my_entry.delete(0,END)
        #Flash up finished message
        my_entry.insert(0,"Finished!")    

def clear_all():
    my_entry.delete(0,END)
    my_label.config(image='')

#create GUI
my_entry=Entry(root,font=("Helvetica",18))
my_entry.pack(pady=20)

my_button=Button(root, text="Create QR", command=create_code,bg="light green",width=8,height=2)
my_button.pack(pady=20)

my_button2=Button(root, text="Clear", command=clear_all,bg="yellow",width=8,height=2)
my_button2.pack(pady=20)

my_label=Label(root,text='')
my_label.pack(pady=20)

root.mainloop()