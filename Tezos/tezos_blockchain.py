import os
import subprocess
import sys
import errno
from collections import defaultdict
from collections import Counter
sys.path.append('/home/ruth/NFT-study/Ruth')
from utils import *
import json
import time

#" https://mainnet-tezos.giganode.io",

def get_blocks(start, end): 
    # start and end can be dates or blocks number
    for curr_start in range(start, end):
        curr_end = curr_start + 1
        if curr_end > end:
            curr_end = end
        blocks_name = f'{curr_start}_{curr_end}'
        #time.sleep(100)
    
        cmd = [
        "tezosetl",
        "export",
        "--start-block",
        str(curr_start),
        "--end-block",
        str(curr_end),
        "--provider-uri",
        "https://mainnet-tezos.giganode.io"
        ]
        process = subprocess.Popen(cmd, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        #time.sleep(10)
        if process.stdout:
            for line in iter(process.stdout.readline, ''):
                print(line,end='')
                sys.stdout.flush()
            process.wait()

def get_tx():
    platforms = {'tz1Y1j7FK1X9Rrv2VdPz5bXoU7SszF8W1RnK':'Hicetnunc','KT1A5P4ejnLix13jtadsfV9GCnXLMNnab8UT':'Kalamint',
    'KT1PKvHNWuWDNVDtqjDha4AostLrGDu4G1jy':'Bazaar Market', 'KT1MxGrhSmLPe4W842AutygvuoxUejLJDuWq':'ByteBlock',
    'KT1FvqJwEDWb1Gwc55Jd1jjTHRVWbYKUUpyq':'OBJKT.com'}
    addresses = defaultdict(int)
    filename = '/home/ruth/NFT-study/Ruth/Tezos/result.json'
    with open(filename,'r') as file:
        for line in file:
            try:
                tx = json.loads(line)
                #print(tx)
                dest = tx['destination']
                if dest in platforms:
                    addresses[platforms[dest]] += 1
            except: 
                pass
    #new_dict = dict(Counter(addresses).most_common(5))
    #new_dict_value = sum(new_dict.values())
    #new_dict['other'] = sum(addresses.values())-new_dict_value
    directory = os.getcwd()

    draw_bar('Transactions number of different platforms',addresses.keys(),addresses.values(),'Platforms','Number','Tezos-number',directory)

    
if __name__ == "__main__":
    start = 1300000    
    end = 1799713  
    get_blocks(start,end)
    #get_tx()

