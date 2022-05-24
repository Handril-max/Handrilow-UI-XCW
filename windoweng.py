# py:3
# HandrilOS Handrilsoft2021
# HFS_tkinter_GUImode_of_Hanchen_Architecture
# window engine
# Handril PC screen
# -*- coding:utf-8 -*-
import os
import sys
import time
import psutil
import six
import shutil
import string
import glob
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image, ImageFilter
from pywifi import const, PyWiFi, Profile
from tkinter import filedialog
from shutil import *
#from HandrilowOSLauncherCode import cpupack as cpk
#import cpupack as cpk

# 窗口容器大小定义


def screensize(root, sw, sh, num1, num2):
    x = num1
    y = num2
    root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
# 全屏关键


def fullscreen(root):
    root.overrideredirect(True)


def winscreen(root):
    root.overrideredirect(False)

# 窗口不可改变大小


def unsize(root):
    root.resizable(0, 0)

# 动画
# 渐显和渐隐动画 （已验证）


def gradually_a_in(assembly, root, num1, num2):  # 渐显动画(固定值)
    for i in range(0, 105, 5)[::1]:
        assembly.place(x=num1, y=num2)
        root.attributes('-alpha', i/100)
        time.sleep(0.01)
        root.update()


def gradually_a_out(assembly, root, num1, num2):  # 渐隐动画(固定值)
    for i in range(0, 105, 5)[::-1]:
        assembly.place(x=num1, y=num2)
        root.attributes('-alpha', i/100)
        root.update()
# 窗口级别动画


def gradually_b_in(root, num1, num2, num3):  # 渐显动画(固定值)
    for i in range(num1, num2, num3)[::1]:
        root.attributes('-alpha', i/100)
        time.sleep(0.01)
        root.update()


def gradually_b_out(root, num1, num2, num3):  # 渐隐动画(固定值)
    for i in range(num1, num2, num3)[::-1]:
        root.attributes('-alpha', i/100)
        root.update()

# 移除和移入动画（已验证）


def move_in(assembly, num1, num2, num3):
    # assembly:控件名称
    for i in range(num1, num2):
        assembly.place(x=i, y=num3)
        assembly.update()


def move_out(assembly, num1, num2, num3):
    # assembly:控件名称
    for i in range(num1, num2)[::-1]:
        assembly.place(x=i, y=num3)
        assembly.update()


def move_where_in(assembly, where, num0, num1, num2):
    # 纵向入
    for i in range(num1, num2):
        assembly.pack(side=where, padx=num0, pady=i)
        time.sleep(0.01)
        assembly.update()


def move_where_out(assembly, where, num0, num1, num2):
    # 纵向出
    for i in range(num1, num2)[::-1]:
        assembly.pack(side=where, padx=num0, pady=i)
        time.sleep(0.01)
        assembly.update()
######################################


def move_p_in(assembly, num0, num1, num2):
    # 纵向入
    for i in range(num1, num2):
        assembly.pack(padx=num0, pady=i)
        time.sleep(0.01)
        assembly.update()


def move_p_out(assembly, num0, num1, num2):
    # 纵向出
    for i in range(num1, num2)[::-1]:
        assembly.pack(padx=num0, pady=i)
        time.sleep(0.01)
        assembly.update()


def move_q_in(assembly, where, num1, num2, num3):
    # 横向入
    for i in range(num1, num2):
        assembly.pack(side=where, padx=i, pady=num3)
        time.sleep(0.005)
        assembly.update()


def move_q_out(assembly, where, num1, num2, num3):
    # 横向出
    for i in range(num1, num2)[::-1]:
        assembly.pack(side=where, padx=i, pady=num3)
        time.sleep(0.005)
        assembly.update()


def fathermovein(root, num1, num2, num3, x, y, sh):
    # 横向移入
    for i in range(num1, num2, num3)[::1]:
        root.geometry(str(i)+'x%d+%d+%d' % (sh, x, y))
        root.update()
        time.sleep(0.015)


def fathermoveout(root, num1, num2, num3, x, y, sh):
    # 横向移出
    for i in range(num1, num2, num3)[::-1]:
        root.geometry(str(i)+'x%d+%d+%d' % (sh, x, y))
        root.update()
        time.sleep(0.015)

# 顶栏中间部分(待修改)


def topdock(inputto1, inputto2, inputto3, inputto4, inputto5):
    import colorlib as hcol
    import date
    import time
    import colorlib
    A2 = 'white'
    A3 = colorlib.cola3()
    A4 = '#F0F0F0'
    A5 = A4
    A7 = A4
    A8 = colorlib.cola8()
    root = topmenuworkWindow()
    root['background'] = A4
    root.attributes('-transparentcolor', '#F0F0F0')
    swc = root.winfo_screenwidth()
    shc = root.winfo_screenheight()
    sw = swc
    swcstr = str(root.winfo_screenwidth())
    #sh = round(shc*(20/768))
    shd = date.topheight()
    sh = shd
    if swcstr > '1600':
        x = (290/swc)*swc
    else:
        x = (250/swc)*swc
    y = 0
    root.geometry('%dx%d+%d+%d' % (sw, sh, x, y))
    root.overrideredirect(True)
    m3 = tk.PanedWindow(root, orient="vertical", bg=A5, width=1)
    m3.pack(fill="both", expand=1)

    file = tk.Label(m3, text=inputto1, fg=A2, width=None,
                    height=None, bd=0, bg=A5, font=('微软雅黑', 10))
    for i in range(5, 10)[::-1]:
        file.pack(side='left', padx=i, pady=1)
        time.sleep(0.01)
        file.update()

    file = tk.Label(m3, text=inputto2, fg=A2, width=None,
                    height=None, bd=0, bg=A5, font=('微软雅黑', 10))
    for i in range(5, 10)[::-1]:
        file.pack(side='left', padx=i, pady=1)
        time.sleep(0.01)
        file.update()

    file = tk.Label(m3, text=inputto3, fg=A2, width=None,
                    height=None, bd=0, bg=A5, font=('微软雅黑', 10))
    for i in range(5, 10)[::-1]:
        file.pack(side='left', padx=i, pady=1)
        time.sleep(0.01)
        file.update()

    file = tk.Label(m3, text=inputto4, fg=A2, width=None,
                    height=None, bd=0, bg=A5, font=('微软雅黑', 10))
    for i in range(5, 10)[::-1]:
        file.pack(side='left', padx=i, pady=1)
        time.sleep(0.01)
        file.update()

    file = tk.Label(m3, text=inputto5, fg=A2, width=None,
                    height=None, bd=0, bg=A5, font=('微软雅黑', 10))
    for i in range(5, 10)[::-1]:
        file.pack(side='left', padx=i, pady=1)
        time.sleep(0.01)
        file.update()

    root.mainloop()


# 窗口
class calenderWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=0.9, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层

        def move(_):
            self.bind('<B1-Motion>', self._on_move)
        self.bind('<Double-Button-1>', move)

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))

    def _on_move(self, event):
        offset_x = event.x_root - self.root_x
        offset_y = event.y_root - self.root_y
        if self.width and self.height:
            geo_str = "%sx%s+%s+%s" % (self.width, self.height,
                                       self.abs_x + offset_x, self.abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (self.abs_x + offset_x, self.abs_y + offset_y)
            self.geometry(geo_str)

        def _on_tap(self, event):
            self.root_x, self.root_y = event.x_root, event.y_root
            self.abs_x, self.abs_y = self.winfo_x(), self.winfo_y()


class menuWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=0.9, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        # self.wm_attributes("-topmost", topmost) # 永远处于顶层

        def move(_):
            self.bind('<B1-Motion>', self._on_move)
        self.bind('<Double-Button-1>', move)

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))

    def _on_move(self, event):
        offset_x = event.x_root - self.root_x
        offset_y = event.y_root - self.root_y
        if self.width and self.height:
            geo_str = "%sx%s+%s+%s" % (self.width, self.height,
                                       self.abs_x + offset_x, self.abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (self.abs_x + offset_x, self.abs_y + offset_y)
            self.geometry(geo_str)

        def _on_tap(self, event):
            self.root_x, self.root_y = event.x_root, event.y_root
            self.abs_x, self.abs_y = self.winfo_x(), self.winfo_y()


class topmenuWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=1, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))


class logWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=0.9, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))


class topmenuworkWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=1, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))


class buttommenuWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=0.9, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))


class messageWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=0.9, bg="#FFFFFF", width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        self.bind('<B3-Motion>', self._on_move)

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))

    def _on_move(self, event):
        offset_x = event.x_root - self.root_x
        offset_y = event.y_root - self.root_y
        if self.width and self.height:
            geo_str = "%sx%s+%s+%s" % (self.width, self.height,
                                       self.abs_x + offset_x, self.abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (self.abs_x + offset_x, self.abs_y + offset_y)
            self.geometry(geo_str)

        def _on_tap(self, event):
            self.root_x, self.root_y = event.x_root, event.y_root
            self.abs_x, self.abs_y = self.winfo_x(), self.winfo_y()


class Dock(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=0.9, bg="black", width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        #self.bind('<B3-Motion>', self._on_move)

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))


class DragWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=1, bg="gray", width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        self.bind('<B3-Motion>', self._on_move)

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))

    def _on_move(self, event):
        offset_x = event.x_root - self.root_x
        offset_y = event.y_root - self.root_y
        if self.width and self.height:
            geo_str = "%sx%s+%s+%s" % (self.width, self.height,
                                       self.abs_x + offset_x, self.abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (self.abs_x + offset_x, self.abs_y + offset_y)
            self.geometry(geo_str)

        def _on_tap(self, event):
            self.root_x, self.root_y = event.x_root, event.y_root
            self.abs_x, self.abs_y = self.winfo_x(), self.winfo_y()


class DragWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=1, bg="white", width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        self.bind('<B3-Motion>', self._on_move)

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))

    def _on_move(self, event):
        offset_x = event.x_root - self.root_x
        offset_y = event.y_root - self.root_y
        if self.width and self.height:
            geo_str = "%sx%s+%s+%s" % (self.width, self.height,
                                       self.abs_x + offset_x, self.abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (self.abs_x + offset_x, self.abs_y + offset_y)
            self.geometry(geo_str)

        def _on_tap(self, event):
            self.root_x, self.root_y = event.x_root, event.y_root
            self.abs_x, self.abs_y = self.winfo_x(), self.winfo_y()


class HandrilWindow(tk.Tk):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=1, bg="gray", width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层
        tk.Label(self,text='划过横条以开始',bg='white',fg='black').pack(side='bottom')

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))


class H_Battery_Drage_Window(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=1, bg="gray", width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))


class appWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=0.9, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层

        self.bind('<B3-Motion>', self._on_move)

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))

    def _on_move(self, event):
        offset_x = event.x_root - self.root_x
        offset_y = event.y_root - self.root_y
        if self.width and self.height:
            geo_str = "%sx%s+%s+%s" % (self.width, self.height,
                                       self.abs_x + offset_x, self.abs_y + offset_y)
        else:
            geo_str = "+%s+%s" % (self.abs_x + offset_x, self.abs_y + offset_y)
            self.geometry(geo_str)

        def _on_tap(self, event):
            self.root_x, self.root_y = event.x_root, event.y_root
            self.abs_x, self.abs_y = self.winfo_x(), self.winfo_y()


class handriltopmenuWindow(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=1, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))


class whitetype(tk.Toplevel):
    root_x, root_y, abs_x, abs_y = 0, 0, 0, 0
    width, height = None, None

    def __init__(self, topmost=True, alpha=1, bg=None, width=None, height=None):
        super().__init__()
        self["bg"] = bg
        self.width, self.height = width, height
        self.overrideredirect(True)
        self.wm_attributes("-alpha", alpha)  # 透明度
        self.wm_attributes("-toolwindow", True)  # 置为工具窗口
        self.wm_attributes("-topmost", topmost)  # 永远处于顶层

    def set_display_postion(self, offset_x, offset_y):
        self.geometry("+%s+%s" % (offset_x, offset_y))

    def set_window_size(self, w, h):
        self.width, self.height = w, h
        self.geometry("%sx%s" % (w, h))
