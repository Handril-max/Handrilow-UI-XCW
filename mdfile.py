import os
import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askdirectory
import cpupack as cpk
import windoweng
from windoweng import *

class createFile(object):
    """
    设计创建文件和文件夹
    """
    def __init__(self,master):
        
        master.title('创建文件v1.0')
        master.geometry('400x380')

        self.path = StringVar()
        self.folder = StringVar()

        Label(master,text = "目标路径:").place(x=50, y= 250)
        Entry(master, textvariable = self.path).place(x=110, y= 250)
        Button(master, text = "路径选择", command = self.selectPath).place(x=265, y= 250)


        Label(master,text = "文件名:").place(x=50, y= 300)
        Entry(master,textvariable = self.folder).place(x=110, y= 300)
        Button(master, text = "确定", command = self.create_file).place(x=265, y= 300)
        cpk.atp(master)

    def selectPath(self):
        path_ = askdirectory()
        self.path.set(path_)

    def create_file(self):
        #print(self.folder.get())  #捕捉用户输入信息
        #print(self.path.get())    #捕捉用户输入信息

        dirs = self.path.get() + "\\"+self.folder.get()
        if not os.path.exists(dirs):
            os.makedirs(dirs)
            file = open(dirs+'\\'+self.folder.get()+".md","w")
            file.write("file name is "+self.folder.get()+" author:Applezhang")
            #弹窗文件名创建成功
            tkinter.messagebox.showinfo('提示','文件名创建成功')
        
        else:
            #弹窗文件文件创建失败
            tkinter.messagebox.showerror('提示','文件名存在，请换一个')

def main():   
    root = appWindow()
    app = createFile(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
    

