import psutil
import os
from HandrilowOSLauncherCode import cpupack as cpk
def main():
    info = psutil.virtual_memory()
    a = '内存占比：'+ str(info.percent)
    cpk.unpathfilewrite("toptipMessage.message", "w",a)

