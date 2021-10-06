import os
import subprocess
import sys
from web3 import Web3

START_BLOCK=13300000 
END_BLOCK=13310000 
STEP_SIZE = 10000


for curr_start in range(START_BLOCK, END_BLOCK, 100000):
    curr_end = curr_start + 99999 # changed from 9
    if curr_end > END_BLOCK:
        curr_end = END_BLOCK
    blocks_name = f'{START_BLOCK}_{END_BLOCK}'

cmd = [
            "ethereumetl",
            "export_blocks_and_transactions",
            "--start-block",
            str(curr_start),
            "--end-block",
            str(curr_end),
            "--transactions-output",
            f"{curr_start}_{curr_end}.csv",
            "--provider-uri",
            "http://127.0.01:8646"
    ]

process = subprocess.Popen(cmd, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
if process.stdout:
    for line in iter(process.stdout.readline, ''):
        print(line,end='')
        sys.stdout.flush()
    process.wait()

