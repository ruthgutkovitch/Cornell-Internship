from web3 import Web3
import pandas as pd
import csv
from runner_tx import *
sys.path.append('/home/ruth/NFT-study/Ruth')
from utils import *

w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8646'))
#w3 = Web3(Web3.HTTPProvider('http://localhost:8646'))

START_BLOCK=13428000
END_BLOCK=13478000 
STEP_SIZE=50000

openSea_Contract = '0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'.lower()
res = "b''"

def getCode(file_name):
    contract , private = 0, 0
    
    with open('result.txt','w') as file:
        with open(file_name, 'r') as file1:
            reader = pd.read_csv(file1)
            for row in reader.itertuples():
                address = w3.toChecksumAddress(str(row.from_address))
                code = w3.eth.getCode(address)
                if str(code)=="b''":
                    private += 1
                else: 
                    contract += 1
            
                file.write(str(code)+"\n")
       
    values = [contract, private]
    print(values)
    return values



if __name__ == "__main__":
    get_blocks_and_transactions(START_BLOCK, END_BLOCK, STEP_SIZE)
    get_token_transfers(START_BLOCK, END_BLOCK, STEP_SIZE)
    res_token = getCode('token_transfers.csv')
    res_tx = getCode('transactions.csv')
    result = [0] * 2
    for i in range(2):
        result[i] = res_token[i] + res_tx[i]
    names = ["Contracts", "Private address"]

    draw_pie('Smart contract vs Private address',result,names,'Contracts',os.getcwd())
    
