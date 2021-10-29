import os
import subprocess
import sys
import pandas as pd
import errno



def get_blocks_and_transactions(START_BLOCK: int, END_BLOCK: int, STEP_SIZE: int):    
    # creates empty csv file with columns only
    #if (not os.path.exists(f'{START_BLOCK}_{END_BLOCK}.csv')):
     #   df = pd.DataFrame(columns=['hash','nonce','block_hash','block_number','transaction_index','from_address','to_address','value','gas','gas_price','input','block_timestamp','max_fee_per_gas','max_priority_fee_per_gas','transaction_type'])
      #  df.to_csv(f'{START_BLOCK}_{END_BLOCK}.csv', index=False)

    # can remove 'else'' if you want to append existing file
    #else:
       # print('file already exists!')
        #raise errno.EEXIST

    blocks_filename = 'blocks.csv'
    transaction_filename = 'transactions.csv'
    
    for curr_start in range(START_BLOCK, END_BLOCK, STEP_SIZE):
        curr_end = curr_start + STEP_SIZE - 1
        if curr_end > END_BLOCK:
            curr_end = END_BLOCK
        tx_name = f'{curr_start}_{curr_start}' #instead of transaction_filename

        cmd = [
                "ethereumetl",
                "export_blocks_and_transactions",
                "--start-block",
                str(curr_start),
                "--end-block",
                str(curr_end),
                "--transactions-output",
                transaction_filename,
                "--provider-uri",
                "http://127.0.01:8646"
        ]
        #"--blocks-output",
         # blocks_filename 

        process = subprocess.Popen(cmd, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if process.stdout:
            for line in iter(process.stdout.readline, ''):
                print(line,end='')
                sys.stdout.flush()
            process.wait()

def get_token_transfers(START_BLOCK: int, END_BLOCK: int, STEP_SIZE: int):
    get_receipt_and_logs(START_BLOCK, END_BLOCK, STEP_SIZE)
    for curr_start in range(START_BLOCK, END_BLOCK, STEP_SIZE):
        curr_end = curr_start + STEP_SIZE - 1
        if curr_end > END_BLOCK:
            curr_end = END_BLOCK
        tx_name = 'token_transfers' + f'{curr_start}_{curr_start}'

        cmd = [
                "ethereumetl",
                "extract_token_transfers",
                "--logs",
                "logs.csv",
                "--output",
                "token_transfers.csv"
        ]

        process = subprocess.Popen(cmd, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if process.stdout:
            for line in iter(process.stdout.readline, ''):
                print(line,end='')
                sys.stdout.flush()
            process.wait()



def get_column_from_transaction(START_BLOCK: int, END_BLOCK: int, STEP_SIZE: int):
    transaction_hashes_filename = 'trans_hashes.txt'
    transaction_filename = 'transactions.csv'

    cmd2 = [
                "ethereumetl",
                "extract_csv_column",
                "--input",
                transaction_filename,
                "--column",
                "hash",
                "--output",
                transaction_hashes_filename
        ]

    process2 = subprocess.Popen(cmd2, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if process2.stdout:
        for line in iter(process2.stdout.readline, ''):
                print(line,end='')
                sys.stdout.flush()
        process2.wait()

def get_receipt_and_logs(START_BLOCK, END_BLOCK, STEP_SIZE):
    get_column_from_transaction(START_BLOCK, END_BLOCK, STEP_SIZE)
    transaction_hashes_filename = 'trans_hashes.txt'
    receipts_filename = 'receipts.csv'
    cmd3= [
            "ethereumetl",
            "export_receipts_and_logs",
            "--transaction-hashes",
            transaction_hashes_filename,
            "--provider-uri",
            "http://127.0.01:8646",
            "--receipts-output",
            receipts_filename,
            "--logs-output",
            "logs.csv"
    ]
    process3 = subprocess.Popen(cmd3, bufsize=1, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if process3.stdout:
        for line in iter(process3.stdout.readline, ''):
                print(line,end='')
                sys.stdout.flush()
        process3.wait()
        
