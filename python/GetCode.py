from web3 import Web3

w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8646'))
START_BLOCK=13176499
END_BLOCK=13376499 
STEP_SIZE=200000

contract , private = 0, 0
get_blocks_and_transactions(START_BLOCK, END_BLOCK, STEP_SIZE)
with open('/home/ruth/NFT-study/Ruth/transactions.csv','r') as file:
    reader = pd.read_csv(file_r,sep=',')
    for row in reader.itertuples():
        code = w3.eth.get_code(row.hash)
        if code=='0x': private += 1
        else: contract += 1

values = [contract, private]
names = ["Contracts", "Private address"]

draw_pie('Smart contract vs Private address',values,names,'Contracts' )

