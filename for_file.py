# -*- coding: utf-8 -*-
import os
from TkinterDnD2 import *
from tkinter import *
import PIL
from PIL import *
from PIL import ImageTk, Image, ImageFilter
def main():
    fath_path = os.getcwd()
    root = Toplevel()
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    root.withdraw()
    root.title('TkinterDnD2 拖拽演示')
    root.grid_rowconfigure(1, weight=1, minsize=600)
    root.grid_columnconfigure(0, weight=1, minsize=sh)
    ###############################################################################################################################
    def resize(image):
        w, h = image.size
        mlength = max(w, h)
        mlength1 = min(w, h)
        mul = sw/mlength
        mul1 = sh/mlength1
        w1 = int(w * mul)
        h1 = int(h * mul1)
        return image.resize((w1, h1))

    file_icon = PhotoImage(file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/FILE.png")
    folder_icon= PhotoImage(file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/FOLD.png")
    word_icon= PhotoImage(file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/WORD.png")
    py_icon= PhotoImage(file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/PY.png")
    pic_icon= PhotoImage(file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/PIC.png")
    html_icon= PhotoImage(file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/HTML.png")
    mic_icon= PhotoImage(file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/MIC.png")
    ppt_icon= PhotoImage(file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/PPT.png")
    css_icon= PhotoImage(file=fath_path + "/HandrilowOSLauncherCode/H_icon/filestype/CSS.png")

    canvas = Canvas(root, name='dnd_demo_canvas', bg='green', relief='sunken',
                    bd=0, takefocus=True, width=600)
    canvas.grid(row=1, column=0, padx=5, pady=5, sticky='news')
    canvas.config(highlightthickness=0)
    image = Image.open(fath_path + '/HandrilowOSLauncherCode/H_icon/H_bg/BG.png')
    im=image.filter(ImageFilter.GaussianBlur(radius=20))
    re_image = resize(image)
    img = ImageTk.PhotoImage(re_image)
    canvas.create_image(sw/2, sh/2, anchor='center', image=img)
    # store the filename associated with each canvas item in a dictionary
    canvas.filenames = {}
    # store the next icon's x and y coordinates in a list
    canvas.nextcoords = [50, 20]
    # add a boolean flag to the canvas which can be used to disable
    # files from the canvas being dropped on the canvas again
    canvas.dragging = False

    def add_file(filename):
        icon = file_icon
        file2,type2=os.path.splitext(filename)
        if os.path.isdir(filename):
            icon = folder_icon
        elif type2=='.doc' or type2=='.docx':
            icon = word_icon
        elif type2=='.py' or type2=='.PY':
            icon = py_icon
        elif type2=='.png' or type2=='.jpg'or type2=='.jpeg'or type2=='.gif':
            icon = pic_icon
        elif type2=='.pptx':
            icon = ppt_icon
        elif type2=='.mp3' or type2=='.wav':
            icon = mic_icon
        elif type2=='.html':
            icon = html_icon
        elif type2=='.css':
            icon = css_icon
            
        id1 = canvas.create_image(canvas.nextcoords[0], canvas.nextcoords[1],
                                    image=icon, anchor='n', tags=('file',))
        id2 = canvas.create_text(canvas.nextcoords[0], canvas.nextcoords[1] + 45,
                                    text=os.path.basename(filename), anchor='n',
                                    justify='center', width=90,fill='white')
    ################################################################################################################################
        def select_item(ev):
            print(canvas.filenames[id2])
            os.startfile(canvas.filenames[id2])  # 打开文件
            canvas.select_from(id2, 0)
            canvas.select_to(id2, 'end')
        canvas.tag_bind(id1, '<ButtonPress-1>', select_item)
        canvas.tag_bind(id2, '<ButtonPress-1>', select_item)
        canvas.filenames[id1] = filename
        canvas.filenames[id2] = filename
        if canvas.nextcoords[0] > 450:
            canvas.nextcoords = [50, canvas.nextcoords[1] + 80]
        else:
            canvas.nextcoords = [canvas.nextcoords[0] + 100, canvas.nextcoords[1]]
    ################################################################################################################################
    # drop methods

    def drop_enter(event):
        print('drop_enter')
        event.widget.focus_force()
        print('Entering %s' % event.widget)
        return event.action

    def drop_position(event):
        print('drop_position')
        return event.action

    def drop_leave(event):
        print('drop_leave')
        print('Leaving %s' % event.widget)
        return event.action

    def drop(event):
        if canvas.dragging:
            # the canvas itself is the drag source
            return REFUSE_DROP
        if event.data:
            files = canvas.tk.splitlist(event.data)
            for f in files:
                add_file(f)
        return event.action

    #canvas.drop_target_register(DND_FILES)
    canvas.dnd_bind('<<DropEnter>>', drop_enter)
    canvas.dnd_bind('<<DropPosition>>', drop_position)
    canvas.dnd_bind('<<DropLeave>>', drop_leave)
    canvas.dnd_bind('<<Drop>>', drop)
    for file in os.listdir(fath_path + "/desktop/"):
        print(fath_path + "/desktop/" + file)
        add_file(fath_path + "/desktop/" + file)
    #add_file(nowpath)

    # drag methods

    def drag_init(event):
        data = ()
        sel = canvas.select_item()
        if sel:
            # in a decent application we should check here if the mouse
            # actually hit an item, but for now we will stick with this
            data = (canvas.filenames[sel],)
            canvas.dragging = True
            return ((ASK, COPY), (DND_FILES, DND_TEXT), data)
        else:
            # don't start a dnd-operation when nothing is selected; the
            # return "break" here is only cosmetical, return "foobar" would
            # probably do the same
            return 'break'

    def drag_end(event):
        # reset the "dragging" flag to enable drops again
        canvas.dragging = False

    #canvas.drag_source_register(1, DND_FILES)
    canvas.dnd_bind('<<DragInitCmd>>', drag_init)
    canvas.dnd_bind('<<DragEndCmd>>', drag_end)

    root.update_idletasks()
    root.deiconify()
    root.mainloop()

