import os
import subprocess
import sys
import pandas as pd
import errno



def get_blocks(start, end): 
    # start and end can be dates or blocks number
    # creates empty csv file with columns only
    if (not os.path.exists(f'{start}_{end}.csv')):
        df = pd.DataFrame()
        df.to_csv(f'{start}_{end}.csv', index=False)
    else:
        print('file already exists!')
        raise errno.EEXIST

    blocks_filename = 'blocks.csv'
    #transaction_filename = 'transactions.csv'
    
    cmd = [
        "tezosetl",
        "export_partitioned",
        "--start",
        str(start),
        "--end",
        str(end),
        "--provider-uri",
        " https://mainnet-tezos.giganode.io",
        "--output-dir",
        blocks_filename
    ]

    process = subprocess.Popen(cmd, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if process.stdout:
        for line in iter(process.stdout.readline, ''):
            print(line,end='')
            sys.stdout.flush()
        process.wait()

if __name__ == "__main__":
    start = 1795705  
    end = 1795706 
    get_blocks(start,end)