from tkinter import *
from tkinter.messagebox import * #弹出提示框的模块
from tkinter.filedialog import * #打开文件对话框,获取文件路径的模块
import os #有关文件夹的模块
import tkinter as tk
from PIL import ImageTk, Image, ImageFilter
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import windoweng


def main():
    root = tk.Toplevel()
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    sw = root.winfo_screenwidth()/2
    sh = root.winfo_screenheight()-120
    x = (swc-sw)/2
    y = (shc-sh)/2
    
    cpk.fathersize(root,sw,sh,x,y)
    root.overrideredirect(True)
    filename = ''
    #在主窗口放置文本
    textPad = Text(root,undo = True)
    textPad.pack(expand = YES,fill = BOTH)
    
    def exite():
        root.destroy()
    
    
    
    
    scroll = Scrollbar(textPad)
    textPad.config(yscrollcommand = scroll.set)
    scroll.config(command = textPad.yview)
    scroll.pack(side = RIGHT,fill = Y)
    """创建菜单栏"""
    menubar = Menu(root)

    def new():
        global filename,textPad,root
        root.title('这是个还未命名的文件')
        filename = None
        #清空文本
        textPad.delete(1.0,END)


    def myopen():
        #因为需要修改到全局变量的值,需要加global关键字
        global filename
        default_dir = r'D:\python' #设置默认打开路径
        #下面filename返回文件路径
        #打开文件对话框并获取文件路径保存
        filename = askopenfilename(title = u'选择文件',defaultextension = '.txt',initialdir = (os.path.expanduser(default_dir))) #tKinter模块的选择文件,后面的os函数是将其中特殊字符替换成目录
        if filename == '':
            filename=None
        else:
            shortcutbar = Frame(root,height = 25,bg = '#F0F0F0')
            tk.Label(shortcutbar,text="Handril记事本--"+os.path.basename(filename),bg='#F0F0F0',fg='black').pack() 
            shortcutbar.pack(expand = NO,fill = X)#basename()是获取文件路径最后的文件名
            #delete()函数中须为n.n小数形式,代表第n行第几个下标
            textPad.delete(1.0,END)
            f = open(filename,'r')
            #向文本中显示文件中的字符串,同样,insert()中,表示从第一行第一个下标插入
            textPad.insert(1.0,f.read())
            #没有使用with,需要手动关闭
            f.close()


    def save():
        global filename
        try:
            f = open(filename,'w')
        #获取文本中的字符串
            message = textPad.get(1.0,END)
            f.write(message)
            f.close()
        except:
            saveas()

    def saveas():
        global filename
    #打开保存文件的文件对话框
        f = asksaveasfilename(initialfile = '未命名.txt',defaultextension = '.txt') #打开文件对话框并获取文件路径保存
        filename = f
        fh = open(f,'w')
        message = textPad.get(1.0,END)
        fh.write(message)
        fh.close()
        root.title("Carson记事本--"+os.path.basename(filename))

    def undo():
        global textPad
        textPad.event_generate("<<Undo>>")

    def redo():
        global textPad
        textPad.event_generate("<<Redo>>")

    def cut():
        global textPad
        textPad.event_generate("<<Cut>>")

    def copy():
        global textPad
        textPad.event_generate("<<Copy>>")

    def paste():
        global textPad
        textPad.event_generate("<<Paste>>")

    def find():
        global root
        t = Toplevel(root)
        t.title('查找')
        t.geometry("260x60+200+250")
        t.transient(root) #告诉root新建t窗口是暂时等待
        Label(t,text = '查找').grid(row = 0,column = 0,sticky = W)
        v = StringVar()
        e = Entry(t,width = 20,textvariable = v)
        e.grid(row =0,column = 1,padx = 2,pady = 2,sticky = 'we')
        e.focus_set() #焦点聚集在此输入框
        c = IntVar()
        Checkbutton(t,text = '不区分大小写',variable = c).grid(row = 1,column = 1,sticky = E)
        Button(t,text = '查找所有',command = lambda :search(v.get(),c.get(),textPad,t,e)).grid(row = 0,column = 2,sticky = 'e'+'w',padx = 2,pady =2)
        def close_search():
            textPad.tag_remove('match','1.0',END)
            t.destroy()
        t.protocol('WM_DELETE_WINDOW',close_search)

    def search(needle,cssnstv,textPad,t,e):
        textPad.tag_remove('match','1.0',END)
        count = 0
        if needle:
            pos = '1.0'
            while True:
                pos = textPad.search(needle,pos,nocase = cssnstv,stopindex=END)
                if not pos:
                    break
                lastpos = pos +str(len(needle))
                textPad.tag_add('match',pos,lastpos)
                count +=1
                pos = lastpos
            textPad.tag_config('match',foreground = 'yellow',background = 'green')
            e.focus_set()
            t.title(str(count)+'个匹配')

#此函数用于鼠标右键显示菜单的
    def popup(event):
        None



    def select_all():
        global textPad
        #tag_add()：为指定的文本添加Tags
        #tag_config()：可以设置Tags的样式
        textPad.tag_add('sel','1.0','end')

    def author():
        cpk.message('版本','Handril文本编辑v1.0')
    def copyright():
        cpk.message('提示','Copyright@Handrilsoft')

    #创建Top文件菜单及其子菜单并绑定函数
    filemenu = Menu(menubar)
    filemenu.add_command(label = '新建',accelerator = 'Ctrl + N',command=new)
    filemenu.add_command(label = '打开',accelerator = 'Ctrl + O',command = myopen)
    filemenu.add_command(label = '保存',accelerator = 'Ctrl + S',command = save)
    filemenu.add_command(label = '另存为',accelerator = 'Ctrl + Shift + S',command = saveas)
    menubar.add_cascade(label = '文件',menu = filemenu)
    #创建Top编辑菜单及其子菜单并绑定函数,同类之间用下分割线
    editmenu = Menu(menubar)
    editmenu.add_command(label = '撤销',accelerator = 'Ctrl + Z',command = undo)
    editmenu.add_command(label = '重做',accelerator = 'Ctrl + Y',command = redo)
    editmenu.add_separator()
    editmenu.add_command(label = '剪切',accelerator = 'Ctrl + X',command = cut)
    editmenu.add_command(label = '复制',accelerator = 'Ctrl + C',command = copy)
    editmenu.add_command(label = '粘贴',accelerator = 'Ctrl + V',command = paste)
    editmenu.add_separator()
    editmenu.add_command(label = '查找',accelerator = 'Ctrl + F',command = find)
    editmenu.add_command(label = '全选',accelerator = 'Ctrl + A',command = select_all)
    menubar.add_cascade(label = '编辑',menu = editmenu)
    #创建Top关于菜单及其子菜单并绑定函数
    aboutmenu = Menu(menubar)
    aboutmenu.add_command(label = '作者',command = author)
    aboutmenu.add_command(label = '版权',command = copyright) 
    menubar.add_cascade(label = '关于',menu = aboutmenu)

    #将前面的菜单绑定到顶部栏
    root.config(menu = menubar)

    #热键绑定
    textPad.bind("<Control-N>",new)
    textPad.bind("<Control-n>",new)
    textPad.bind("<Control-O>",myopen)
    textPad.bind("<Control-o>",myopen)
    textPad.bind("<Control-S>",save)
    textPad.bind("<Control-s>",save)
    textPad.bind("<Control-A>",select_all)
    textPad.bind("<Control-a>",select_all)
    textPad.bind("<Control-F>",find)
    textPad.bind("<Control-f>",find)

    textPad.bind("<Button-3>",popup)

    def jump2():
        cpk.mwoutto(bottomtype,'bottom',0,8,13)
        exite()
    def jump1(_):
        cpk.mwinto(bottomtype,'bottom',0,8,15)
        jump2()
    def mydock(_):
        exite()
    bottomtype = tk.Label(root,bd=1,width=round(swc*(1/3)),height=3,font=('等线' ,1))
    bottomtype.bind('<Button-1>',mydock)
    bottomtype.bind('<Leave>',jump1)
    #bottomtype.bind('<Enter>',jump1) 
    cpk.mwinto(bottomtype,'bottom',0,0,8)
    
    root.mainloop()


