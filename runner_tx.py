import os
import subprocess
import sys
from web3 import Web3

START_BLOCK=13160000 
END_BLOCK=13199521  

for curr_start in range(START_BLOCK, END_BLOCK, 100000):
    curr_end = curr_start+99999 # changed from 9
    if curr_end > END_BLOCK:
        curr_end = END_BLOCK
    folder_name = f'/home/ruth/NFT-study/Ruth/Transactions/{curr_start}_{curr_end}'
    try:
        os.mkdir(folder_name)
    except:
        pass

cmd = [
            "ethereumetl",
            "export_blocks_and_transactions",
            "--start-block",
            str(curr_start),
            "--end-block",
            str(curr_end),
            "--transactions-output",
            f"{folder_name}.csv",
            "--provider-uri",
            "http://127.0.01:8646"
    ]

process = subprocess.Popen(cmd, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
if process.stdout:
    for line in iter(process.stdout.readline, ''):
        print(line,end='')
        sys.stdout.flush()
    process.wait()

