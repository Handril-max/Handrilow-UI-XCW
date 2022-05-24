#!/usr/bin/env python
# -*- coding:utf-8 -*-
#py:3
#HandrilOS Handrilsoft2021
#HFS_tkinter_GUImode_of_Hanchen_Architecture

import tkinter
from tkinter import ttk
import os
from urllib import request
from HandrilowOSLauncherCode import music
import requests
from HandrilowOSLauncherCode import cpupack as cpk
from HandrilowOSLauncherCode import fileprocess as fp

pidt = "./H_fileprocess/linde.pid"
pids = "./H_fileprocess/lindesearch.pid"


class SearchWindows(tkinter.Frame):
    
    def __init__(self, master):
        self.frame = tkinter.Frame(master, height=600, width=450, bd=1)
        self.songs = None   # 搜索到的所有歌曲(20)的信息
        
        self.frame.pack(side='bottom',pady=15)
        
        self.info = None    # 当前歌曲的信息
        self.fileName = "./Musics/"

        timeout = 60
        output = 'Musics'
        quiet = True
        cookie_path = 'Cookie'
        self.netease = Netease(timeout, output, quiet, cookie_path)

    def run(self):
        self.searchBar()
        self.download()


    # 搜索框
    def searchBar(self):
        entry = tkinter.Entry(self.frame,bd=0)
        entry.place(width=250, height=29, x=30, y=10)

        def getValue(_):
            self.netease.download_song_by_search(entry.get())
            self.songs = self.netease.crawler.result
            self.showSong()
            other1 = tkinter.Label(self.frame,bg="black",width=2, height=100)
            other1.place(x=-1,y=-1)
            
        entry.bind('<Return>',getValue)

    # 显示搜索到的歌曲
    def showSong(self):
        tree = ttk.Treeview(self.frame)
        # 定义列
        tree["columns"] = ("song", "singer", "url")

        # 设置列,列还不显示
        tree.column("song", width=50)
        tree.column("singer", width=50)
        tree.column("url", width=50)

        # 设置表头  和上面一一对应
        tree.heading("song", text="歌曲")
        tree.heading("singer", text="唱者")
        tree.heading("url", text="来源")

        count = len(self.songs)
        for song in reversed(self.songs):
            url = self.netease.crawler.get_song_url(song.song_id)
            tree.insert("", 0, text="Linde", values=(song.song_name,
                                                   song.singer_name, url))
            count -= 1

        # 鼠标选中一行回调
        def selectTree(event):
            for item in tree.selection():
                item_text = tree.item(item, "values")
                self.info = item_text

        # 滚动条
        sy = tkinter.Scrollbar(tree)
        sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        sy.config(command=tree.yview)
        tree.config(yscrollcommand=sy.set)

        # 选中行
        tree.bind('<<TreeviewSelect>>', selectTree)
        tree.place(width=550, height=500,x=-200, y=50)

        
    # 下载选中的歌曲
    def download(self):

        def downloadSong():
            if self.info is None:
                cpk.message("麟德音乐器","该歌曲下载失败")
            else:
                request.urlretrieve(self.info[2],
                            self.fileName+self.info[1]+'-'+self.info[0]+'.mp3')
                cpk.message("麟德音乐器","该音乐下载成功")
        
        # 下载按钮
        downloadBtn = tkinter.Button(self.frame, text="获取", bg="black",fg='white',
                                   command=downloadSong, width=6, height=1,bd=0)

        downloadBtn.place(x=290, y=10)

        def exite():
            cpk.unpathfilewrite("toptip.message","w"," ")
            fp.exitesys(self.frame,pids)
            self.frame.destroy()

        bottom = tkinter.Label(self.frame, bg="#DCDCDC",width=60,height=29,bd=0)
        bottom.place(x=30,y=55)
        
        other1 = tkinter.Label(self.frame,bg="black",width=2, height=100)
        other1.place(x=-1,y=-1)

        other2 = tkinter.Label(self.frame,bg="black",width=100, height=100)
        other2.place(x=350,y=-1)

        exite = tkinter.Button(self.frame, text="| 无操作", bg="black",fg='white',
                                   command=exite, width=6, height=1,bd=0)

        exite.place(x=350, y=10)

        name = tkinter.Label(self.frame, text="Linde Music @ Handrilsoft", bg="#F0F0F0",fg='black',height=1,bd=0)
        name.place(x=30,y=560)
        
