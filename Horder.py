#py:3
#Handrilsoft
#for Horder mould
import tkinter as tk
from tkinter import *
from .import shellcorn
#import shellcorn
import time
from . import cpupack as cpk
from .openHandrilow.sys_windoweng import *
from .openHandrilow import hf_textanaly as hfta
from .openHandrilow.sys_childframe import *
e_name = 'Hanshell'
c_name = '终端'
def main():
    root =HandrilApp(c_name)
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    sw = swc/2
    sh = shc/2
    t_x = (swc-sw)/2
    t_y = (shc-sh)/2
    root.geometry('%dx%d+%d+%d' % (sw, sh, t_x, t_y))
    cpk.unpathfilewrite("apppath.psw", "w", c_name)
    fateher_f = tk.Frame(root,width=sw,height=sh-10)
    fateher_f.place(x=0,y=0)
    enter_top = tk.Frame(fateher_f,width=30)
    enter_top.place(x=5,y=5)
    shell_div = tk.Frame(fateher_f)
    shell_div.place(x=0,y=40)
    
    ico = tk.Label(enter_top,justify='left',text='>_',font=('黑体', 20,'bold'),bg='#003371',fg='white')
    ico.pack(side='left',padx=5)
    tip = tk.Label(enter_top,justify='left',text='''Handrilow XCW Shell
Copyright @ 2109-2022 XIAN China''',font=('黑体', 10))
    tip.pack(side='left')

    bgc = '#392F41'
    fgc = 'white'
    for_lab = tk.Label(shell_div,justify='left',font=('黑体', 12),width=round(swc/15),height=round(shc/30)
                       ,bg=bgc,fg=fgc)
    for_lab.pack(side='bottom')

    
    exter_txt = StringVar()
    def order(_):
        myorder = enter.get()
        cutorder = hfta.cut.icut(myorder)
        print(hfta.cut.icut(myorder))
        if myorder == 'clean':
            for_shell.delete('1.0','end')
        if cutorder[0] == 'adb':
            #cpk.message('ADB','转调ADB')
            if cutorder[2] == 'version':
                for_shell.insert(END,str(shellcorn.main('adb version')))
            if cutorder[2] == 'devices':
                for_shell.insert(END,str(shellcorn.main('adb devices')))
            if cutorder[2] == 'shell':
                if cutorder[4] == 'pm':
                    for_shell.insert(END,str(shellcorn.main('adb shell pm list packages')))
        for_shell.insert(END,str(shellcorn.main(myorder)))
        #for_shell.config(text=shellcorn.main(str(myorder)))
    enter = tk.Entry(for_lab,width=100,bd=0,bg='#392F41',fg='white')
    enter.bind('<Return>',order)
    def cls(_):
        enter.delete(0,"end")
    enter.bind('<Double-Button-1>',cls)
    enter.insert(0,':-)清空并在此输入命令以执行')

    for_shell = tk.Text(for_lab,bg=bgc,fg=fgc,bd=0)
    for_shell.place(x=0,y=30)
    enter.place(x=5,y=5)
    root.mainloop()

