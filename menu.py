from tkinter import *
from PIL import Image,ImageTk
import fitz
class Main:
    def __init__(self,root):
        super().__init__()
        root.geometry("805x500+450+150")
        self.init_main()

    def init_main(self):
        self.btn=Button(text="open widget",command=self.text)
        self.btn.pack()

    def text(self):
        WidgetText(Text)


class WidgetText(Text):
 def __init__(self,root):
     super().__init__()
     self.init_text()
     self.place(x=20,y=40)

 def init_text(self):
     self["width"]=50
     self.img=ImageTk.PhotoImage(file="old-book-texture01.jpg")
     self.image_create(END,image=self.img)

     doc = fitz.open("22074926.a4.pdf")
     for current_page in range(len(doc)):
         page = doc.loadPage(current_page)
         self.insert(END,page.getText("text"))


root=Tk()
Main(root)
root.mainloop()