#py:3
#Handrilsoft
#for Horder mould
import os
def main(order):
    shell = os.popen(order).read()
    return shell

def adb(order):
    shell = os.popen(order).read()
    return shell
