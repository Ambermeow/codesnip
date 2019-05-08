import re
import json
from tqdm import tqdm
# digits 到中文字符的映射
NUM_CNS_low = {'1':'一','2':'二','3':'三','4':'四','5':'五',
               '6':'六','7':'七','8':'八','9':'九','0':'零'}

def dig2low(str_digs):  # 直译 2008 --> 二零零八
    list_cha = [str_ for str_ in str_digs]
    list_cha = [NUM_CNS_low[str_] for str_ in list_cha if str_ in NUM_CNS_low.keys()]
    return ''.join(list_cha)

def single_(str_digs):  # 阿拉伯数字转中文 个位
    return NUM_CNS_low[str_digs]

def tens_(str_digs):    # 阿拉伯数字转中文 十位
    if str_digs == '10':
        numbers = "十"
    elif str_digs[0] == '1' :
        numbers = "十"+single_(str_digs[1])
    elif str_digs[1] == '0':
        numbers = NUM_CNS_low[str_digs[0]]+"十"
    else:
        numbers = NUM_CNS_low[str_digs[0]]+"十"+single_(str_digs[1])
    return numbers

def handred_(str_digs): # 阿拉伯数字转中文 百位
    if str_digs[1:] == '00':
        numbers = str_digs[0]+'百'
    elif str_digs[1] == '0':
        numbers = str_digs[0]+"百零"+str_digs[2]
    else:
        numbers = NUM_CNS_low[str_digs[0]]+"百"+tens_(str_digs[1:])
    return numbers
    
def thousand_(str_digs): # 阿拉伯数字转中文 千位
    if str_digs[1:] == "000":
        numbers = str_digs[0]+'千'
    elif (str_digs[1:3] == '00'):
        numbers = NUM_CNS_low[str_digs[0]]+'千零'+NUM_CNS_low[str_digs[3]]
    elif (str_digs[1] == '0'):
        numbers = NUM_CNS_low[str_digs[0]]+'千零'+tens_(str_digs[2:])
    else:
        numbers = NUM_CNS_low[str_digs[0]]+'千'+handred_(str_digs[1:])
    return numbers




def digs2low(str_digs):  # 把字符的阿拉伯数字的293转成二百九十三
    s = re.findall("\d+",str_digs)[0]
    mag = len(str_digs)
    if mag == 1:
        str_low = single_(str_digs) 
    elif (mag == 2): 
        str_low = tens_(str_digs)      
    elif (mag == 3):
        str_low = handred_(str_digs) 
    elif (mag == 4):
        str_low = thousand_(str_digs)
    return str_low



print(digs2low("11"))
