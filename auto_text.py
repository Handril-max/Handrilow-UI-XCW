#py:3
#Handrilsoft
#About document auto text
import tkinter as tk
from HandrilowOSLauncherCode.openHandrilow.sys_windoweng import *
from HandrilowOSLauncherCode.openHandrilow import document_read
from HandrilowOSLauncherCode.openHandrilow import sys_win_cartoon
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode.openHandrilow import hf_textanaly as hta
from HandrilowOSLauncherCode.openHandrilow import set_path
fath_path = set_path.pwd()

def main():
    cpk.unpathfilewrite("toptipMessage.message", "w", "请选择文档文件")
    file = document_read.select_document()
    title = document_read.doc.title(file)
    cpk.unpathfilewrite("toptipMessage.message", "w", str(title))
    info = document_read.doc.read_fromat(file)
    ##################################################
    root = tk.Toplevel()
    root.wm_attributes("-toolwindow", True)  # 置为工具窗口
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    root.config(cursor='circle')
    root.overrideredirect(True)
    ####################################################
    w_box = 200
    h_box = 200
    def resiz(w, h, w_box, h_box, pil_image):
        f1 = 1.0*w_box/w
        f2 = 1.0*h_box/h
        factor = min([f1, f2])
        width = int(w*factor)
        height = int(h*factor)
        return pil_imag.resize((width, height), Image.ANTIALIAS)
    name = tk.Label(root, text="Taskmgr", width=w_box, height=h_box)
    pil_imag = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/word.png')
    w, h = pil_imag.size
    pil_image_resize = resiz(w, h, w_box, h_box, pil_imag)
    tk_imag = ImageTk.PhotoImage(pil_image_resize)
    name.config(image=tk_imag)
    name.place(x=10,y=10)
    ###################################################
    apptit = tk.Frame(root,wid=sw/4,height=30)
    apptit.place(x=10,y=220)
    apptitle = tk.Label(apptit,text='文本信息',fg='black',font=('等线',17),justify=LEFT)
    apptitle.place(x=0,y=0)
    
    baseinfo = tk.Frame(root,wid=sw/4,height=(sh/2)-10)
    baseinfo.place(x=10,y=260)
    docuinfo = tk.Label(baseinfo,text=info,fg='black',font=('等线',12),justify=LEFT)
    docuinfo.place(x=0,y=0)
    ####################################################
    docu = tk.Frame(root,wid=sw/2,height=sh-60,bg='#D3D3D3')
    docu.place(x=round(sw/4),y=10)
    sys_win_cartoon.display_show(root,1,20,sw,sh,sw,sh-30)
    root.geometry("%dx%d+%d+%d" % (sw, sh-30, 0, 30))
    #####################################################
    info_in_doc = document_read.doc.read_total(file)
    in_doc = tk.Text(docu,fg='black',font=('等线',11),bd=0,bg='#D3D3D3',height=45)
    in_doc.insert("end",info_in_doc)
    in_doc.place(x=20,y=5)
    ####################################################\
    word_sort = hta.word.mostly(hta.cut.icut(info_in_doc),100)
    wst = tk.Label(root,text='相对高频',fg='black',font=('等线',17),justify=LEFT)
    wst.place(x=sw*(3/4)+20,y=10)
    apptitl = tk.Text(root,fg='black',font=('等线',11),width=35,bd=0,bg='#F0F0F0')
    apptitl.insert("end",word_sort)
    apptitl.place(x=sw*(3/4)+20,y=50)
    ####################################################
    #小横条
    def jump2():
        cpk.unpathfilewrite("toptipMessage.message", "w", "")
        sys_win_cartoon.intend_display(root,1,40,sw,sh,sw,sh-30)
        root.destroy()
    def jump1(_):
        jump2()
    bottomtype = tk.Canvas(root,width=sw/3,height=5,bg='black')
    bottomtype.bind('<Leave>',jump1)
    bottomtype.pack(side='bottom',pady=5)

    ####################################################
   
    
    root.mainloop()

