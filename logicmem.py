import os
from HandrilowOSLauncherCode import cpupack as cpk

#基本操作
class FileOperate():
    def unpathfilewrite(filename,statue,result):
        with open(filename,statue,encoding='utf-8') as f:
            f.write(result)
    def pathfilewrite(path,statue):
        filejob = open(path,statue)
        filejob.close()
#基本逻辑
class BeaseLogic():
    #bease###
    def fel(what,sth,sthl,condition1,condition2):
        what
        if sth == sthl:
            condition1
        else:
            condition2
    def felin(what,sth,sthl,condition1,condition2):
        what
        if sth in sthl:
            condition1
        else:
            condition2
    
    def felelif(what,sth,sthl,sth2,sthl2,condition1,condition2):
        what
        if sth == sthl:
            condition1
        elif sth2 == sthl2:
            condition2
            
    def felmorething(what,sth,sthl,condition1):
        what
        if sth == sthl:
            condition1
            
            
    #furthermore###
    def felCompareMorethingMax(what,sth,sthl,condition1):
        what
        if sth >= sthl:
            condition1
    def felCompareMorethingMin(what,sth,sthl,condition1):
        what
        if sth <= sthl:
            condition1
        
    def felCompareMax(what,sth,sthl,condition1,condition2):
        what
        if sth >= sthl:
            condition1
        else:
            condition2     
    def felCompareMin(what,sth,sthl,condition1,condition2):
        what
        if sth <= sthl:
            condition1
        else:
            condition2

    #nowhat###
    def delmorenothing(sth,sthl,condition1):
        if sth == sthl:
            condition1
    def delCompareMorethingMax(sth,sthl,condition1):
        if sth >= sthl:
            condition1
    def delCompareMorethingMin(sth,sthl,condition1):
        if sth <= sthl:
            condition1
    def delCompareMax(what,sth,sthl,condition1,condition2):
        if sth >= sthl:
            condition1
        else:
            condition2     
    def delCompareMin(what,sth,sthl,condition1,condition2):
        if sth == sthl:
            condition1
        else:
            condition2
    def delMorethingIn(sth,sthl,condition1):
        if sth in sthl:
            print("578")
            condition1
        else:
            print("234")
            pass
    def delPrintCompareMorethingMax(sth,sthl,x,condition1):
        if sth >= sthl:
            x = condition1
        return x
    def delPrintCompareMorethingMin(sth,sthl,x,condition1):
        if sth <= sthl:
            x = condition1
        return x
    
    
        
#登录判断
def lockandlogin():
    fileexists = os.path.exists("./HandrilowOSLauncherCode/set/yidong.set")
    BeaseLogic.felelif(fileexists,fileexists,True,cpk.lockpart(),fileexists,False,cpk.f_loglock())
   

#解锁模块
def unlockpart():
    fileexists = os.path.exists("./HandrilowOSLauncherCode/set/lockscreen.set")
    if fileexists == True:
        cpk.top()
    elif fileexists == False:
        None

       
