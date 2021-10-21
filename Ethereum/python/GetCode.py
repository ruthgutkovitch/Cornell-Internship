from web3 import Web3
from utils import *
from runner_tx import *

#w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8646'))
w3 = Web3(Web3.HTTPProvider('http://localhost:8646'))
START_BLOCK=13176499
END_BLOCK=13376499 
STEP_SIZE=200000

openSea_Contract = '0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'.lower()

contract , private = 0, 0
#get_blocks_and_transactions(START_BLOCK, END_BLOCK, STEP_SIZE)
with open('/home/ruth/NFT-study/Ruth/transactions.csv','r') as file:
    reader = pd.read_csv(file,sep=',')
    for row in reader.itertuples():
        #if str(row.to_address)==openSea_Contract:
            address = w3.toChecksumAddress(str(row.from_address))
            print(address)
            code = w3.eth.getCode(address)
            print(code)
            if str(code)=='0x':
                private += 1
                print("1")
            else: 
                contract += 1
                print("2")
            print(row.from_address)
            break

values = [contract, private]
names = ["Contracts", "Private address"]

draw_pie('Smart contract vs Private address',values,names,'Contracts' )

