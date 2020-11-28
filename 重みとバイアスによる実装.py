import numpy as np
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7    #出力信号が１を出力する度合いを決める
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5, -0.5])  #ANDと違う
    b = 0,7                     #ANDと違う
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2                    #ANDと違う
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1