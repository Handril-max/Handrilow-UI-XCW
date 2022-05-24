from HandrilowOSLauncherCode import cpupack as cpk
from time import sleep
from shutil import copytree
from psutil import disk_partitions

def main(): 
    #while True:
        #  设置休眠时间
        sleep(0)
        for item in disk_partitions():
            if 'removable' in item.opts:
                driver, opts = item.device, item.opts
                #  输出可移动驱动器符号
                #cpk.showhide('驱动器：' + driver)
                cpk.unpathfilewrite("deviceinfo,psw","w",driver)
                
                return driver
            #  没有找到可输出驱动器
            else:
                continue
        

def mainbutton(): 
    #while True:
        #  设置休眠时间
        sleep(0)
        for item in disk_partitions():
            if 'removable' in item.opts:
                driver, opts = item.device, item.opts
                #  输出可移动驱动器符号
                cpk.showhide('驱动器：' + driver)
                cpk.unpathfilewrite("deviceinfo,psw","w",driver)
                return driver
            #  没有找到可输出驱动器
            else:
                cpk.showhide('暂无驱动器')
                cpk.unpathfilewrite("deviceinfo,psw","w",'暂无驱动器')
                #continue
        
