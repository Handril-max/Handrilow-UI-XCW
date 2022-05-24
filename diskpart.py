import os
import time
import psutil
from shutil import *
from threading import Thread
from tkinter import filedialog

def mkfile(target):
    file = open(target,'w')
    file.close()
def mkdir(target):
    os.mkdir(target)
        
        
def delete(target):
    if os.path.isfile(target):
        os.remove(target)
    elif os.path.isdir(target):
        os.rmdir(target)
    else:
        None
    
def dir_bat_copy_self(frome,target):
    '''
    frome = frome
    target = target
    '''
    if os.path.exists(target):
        None
    else:
        os.mkdir(target)
    local_device = []
    mobile_device = []
    local_number = 0
    mobile_number = 0
    oldDiskName = [] #旧的磁盘列表
    number = 0 #磁盘数，判断是否为第一次运行
    ''' 
    从sourcepath复制文件和目录到targetPath
    '''
    def copyfile(sourcePath,targetPath,threadName):

        for f in os.listdir(sourcePath):
            if(f == 'System Volume Information'): #过滤系统文件夹
                continue

            f1 = os.path.join(sourcePath,f) #连接源文件（目录）名
            f2 = os.path.join(targetPath,f) #连接目标文件（目录）名

            if os.path.isfile(f1): #如果为文件，则进行复制操作
                file1 = open(f1,'rb')
                file2 = open(f2,'wb')
                print(threadName + '-%s \nCopying...'%(f1))
                file2.write(file1.read())
                print(threadName + '-%s \nCopy successfully!  '%(f1))
            else:                  #如果为目录，创建新一级的目标目录，并递归操作
                print(threadName + '-%s \nList copying...'%(f1))
                print(threadName + '-%s \nMade target list ！'%(f2))
                os.mkdir(f2)
                copyfile(f1,f2,threadName)
                print(threadName + '-%s \nMade target list ！'%(f2))
    '''
    获取磁盘信息，并与上次获取的信息进行比较，判断是否有新的磁盘添加进来
    '''
    def getDiskMessage():
        global oldDiskName #声明全局变量
        global number

        if number == 0: #第一次操作，先获取一遍磁盘数据，然后返回
            for disk in psutil.disk_partitions():
                number = number + 1
                oldDiskName.append(disk.device[:2]) #获取盘符信息
            return

        newDiskName = [] #保存新获取的磁盘信息
        for disk in psutil.disk_partitions():
            newDiskName.append(disk.device[:2]) #获取新的磁盘信息
        
        newDiskList = arrayCompare(oldDiskName,newDiskName) #获取新增盘符列表

        oldDiskName.clear() #清除旧盘符列表
        oldDiskName = newDiskName[:] #复制新盘符列表给旧盘符列表
        return newDiskList
    

    # 更新usb端口状态
    def update():
        tmp_local_number = 0
        tmp_mobile_number = 0
        try:
            part = psutil.disk_partitions()
        except:
            print("程序异常")
            sys.exit()
        for i in range(len(part)):
            tmp_list = part[i].opts.split(',')
            if "fixed" in tmp_list:
                tmp_local_number = tmp_local_number + 1
                local_device.append(part[i].device)
            elif "removable" in tmp_list:
                tmp_mobile_number = tmp_mobile_number + 1
                mobile_device.append(part[i].device)
                pass
            pass
        return '移动磁盘：'+ str(tmp_mobile_number)
    '''
    比较两个磁盘盘符列表，并返回新盘符列表中旧盘符列表没有的盘符名列表
    '''
    def arrayCompare(oldDiskName,newDiskName):
        newDiskList = []
        for name in newDiskName:
            if name not in oldDiskName: #旧盘符中没有，则添加这个到新增盘符列表中
                newDiskList.append(name)
        return newDiskList
    
    '''
    复制盘符name中的文件到目标目录中
    '''
    def copy(name,threadName):
    
        targetRoot = str(target) #目标目录
        timeNow = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))) #获取当前时间字串
        targetPath = os.path.join(targetRoot,name[:1]+'_'+timeNow+'_'+'from'+'_'+'Handrilow') #创建一个新目录，使用目标目录+盘符+时间作为名称，防止重复
        os.mkdir(targetPath) #创建新的目录
        copyfile(name,targetPath,threadName) #复制文件
        print('提示','%s盘 复制成功！'%(name[:1]))
        main()

    #copy all file from other disk
    def boot():
        
        threadCount = 0 #线程计数
        while True:
            newDiskList = [str(frome)]
            print('新磁盘列表：'+str(newDiskList))
            for name in newDiskList: #根据新获取到的数据去复制文件
                copy(name,'@Handrilsoft')
                print('开始复制%s盘文件...'%(name[:1]))
            time.sleep(0)
    boot()

    
def dir_bat_copy_order():
    by='Handrilow Operate System @ Handrilsoft\n景域汉家之阁|含昭科技司'#作者
    print(by)
    frome = input('------------------------------------------------------------\n从这里>>>')
    target = input('到这里>>>')
    if os.path.exists(target):
        None
    else:
        os.mkdir(target)
    local_device = []
    mobile_device = []
    local_number = 0
    mobile_number = 0
    oldDiskName = [] #旧的磁盘列表
    number = 0 #磁盘数，判断是否为第一次运行
    ''' 
    从sourcepath复制文件和目录到targetPath
    '''
    def copyfile(sourcePath,targetPath,threadName):

        for f in os.listdir(sourcePath):
            if(f == 'System Volume Information'): #过滤系统文件夹
                continue

            f1 = os.path.join(sourcePath,f) #连接源文件（目录）名
            f2 = os.path.join(targetPath,f) #连接目标文件（目录）名

            if os.path.isfile(f1): #如果为文件，则进行复制操作
                file1 = open(f1,'rb')
                file2 = open(f2,'wb')
                print(threadName + '-%s \nCopying...'%(f1))
                file2.write(file1.read())
                print(threadName + '-%s \nCopy successfully!  '%(f1))
            else:                  #如果为目录，创建新一级的目标目录，并递归操作
                print(threadName + '-%s \nList copying...'%(f1))
                print(threadName + '-%s \nMade target list ！'%(f2))
                os.mkdir(f2)
                copyfile(f1,f2,threadName)
                print(threadName + '-%s \nMade target list ！'%(f2))
    '''
    获取磁盘信息，并与上次获取的信息进行比较，判断是否有新的磁盘添加进来
    '''
    def getDiskMessage():
        global oldDiskName #声明全局变量
        global number

        if number == 0: #第一次操作，先获取一遍磁盘数据，然后返回
            for disk in psutil.disk_partitions():
                number = number + 1
                oldDiskName.append(disk.device[:2]) #获取盘符信息
            return

        newDiskName = [] #保存新获取的磁盘信息
        for disk in psutil.disk_partitions():
            newDiskName.append(disk.device[:2]) #获取新的磁盘信息
        
        newDiskList = arrayCompare(oldDiskName,newDiskName) #获取新增盘符列表

        oldDiskName.clear() #清除旧盘符列表
        oldDiskName = newDiskName[:] #复制新盘符列表给旧盘符列表
        return newDiskList
    

    # 更新usb端口状态
    def update():
        tmp_local_number = 0
        tmp_mobile_number = 0
        try:
            part = psutil.disk_partitions()
        except:
            print("程序异常")
            sys.exit()
        for i in range(len(part)):
            tmp_list = part[i].opts.split(',')
            if "fixed" in tmp_list:
                tmp_local_number = tmp_local_number + 1
                local_device.append(part[i].device)
            elif "removable" in tmp_list:
                tmp_mobile_number = tmp_mobile_number + 1
                mobile_device.append(part[i].device)
                pass
            pass
        return '移动磁盘：'+ str(tmp_mobile_number)
    '''
    比较两个磁盘盘符列表，并返回新盘符列表中旧盘符列表没有的盘符名列表
    '''
    def arrayCompare(oldDiskName,newDiskName):
        newDiskList = []
        for name in newDiskName:
            if name not in oldDiskName: #旧盘符中没有，则添加这个到新增盘符列表中
                newDiskList.append(name)
        return newDiskList
    
    '''
    复制盘符name中的文件到目标目录中
    '''
    def copy(name,threadName):
    
        targetRoot = str(target) #目标目录
        timeNow = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))) #获取当前时间字串
        targetPath = os.path.join(targetRoot,name[:1]+'_'+timeNow+'_'+'from'+'_'+'Handrilow') #创建一个新目录，使用目标目录+盘符+时间作为名称，防止重复
        os.mkdir(targetPath) #创建新的目录
        copyfile(name,targetPath,threadName) #复制文件
        print('提示','%s盘 复制成功！'%(name[:1]))
        main()

    #copy all file from other disk
    def boot():
        
        threadCount = 0 #线程计数
        while True:
            newDiskList = [str(frome)]
            print('新磁盘列表：'+str(newDiskList))
            for name in newDiskList: #根据新获取到的数据去复制文件
                copy(name,'@Handrilsoft')
                print('开始复制%s盘文件...'%(name[:1]))
            time.sleep(0)
    boot()

