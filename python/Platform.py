import pandas as pd
import csv
from collections import defaultdict
from utils import *
from runner_tx import * 

file = r'/home/ruth/NFT-study/Ruth/transactions.csv'

platforms = {'0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'.lower():'OpenSea','0x60f80121c31a0d46b5279700f9df786054aa5ee5'.lower():'Rarible',
 '0xE052113bd7D7700d623414a0a4585BCaE754E9d5'.lower():'Niftygateway','0x2fE9263BF105095e16167C093C4d28140e936E1b'.lower():'kiwiswap',
 '0x87d73E916D7057945c9BcD8cdd94e42A6F47f776'.lower():'nftx','0x88341d1a8F672D2780C8dC725902AAe72F143B0c'.lower():'nftfi',
 '0xD8E3FB3b08eBA982F2754988d70D57eDc0055ae6'.lower():'zora'}

#nfttrader = ''.lower()
#foundation = ''.lower()
#nft20 = ''.lowe 

ether = lambda value: value / 1e18

START_BLOCK=13276499
END_BLOCK=13376499 
STEP_SIZE=200000

#get_blocks_and_transactions(START_BLOCK, END_BLOCK, STEP_SIZE)


values = defaultdict(int)

with open(file,'r') as file_r:
    reader = pd.read_csv(file_r)
    for row in reader.itertuples():
        address = str(row.to_address).lower()
        if address in platforms:
            values[platforms[address]] += ether(int(row.value))

for key in values:
    values[key] = round(values[key],2)

print(values)


draw_bar('Comparing volume of different platforms',values.keys(),values.values(),'Platforms','Volume','platforms-volume')

#draw_pie('Comparing number of tx of different platforms',values.values(),values.keys(),'platforms-number')