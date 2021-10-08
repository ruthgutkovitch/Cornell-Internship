import pandas as pd
import csv
from collections import defaultdict
from utils import *

file = r'/home/ruth/NFT-study/Ruth/transactions.csv'

platforms = {'0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'.lower():'OpenSea','0x60f80121c31a0d46b5279700f9df786054aa5ee5'.lower():'Rarible',
 '0xE052113bd7D7700d623414a0a4585BCaE754E9d5'.lower():'Niftygateway','0x2fE9263BF105095e16167C093C4d28140e936E1b'.lower():'kiwiswap',
 '0x87d73E916D7057945c9BcD8cdd94e42A6F47f776'.lower():'nftx','0x88341d1a8F672D2780C8dC725902AAe72F143B0c'.lower():'nftfi',
 '0xD8E3FB3b08eBA982F2754988d70D57eDc0055ae6'.lower():'zora'}



#nfttrader = ''.lower()
#foundation = ''.lower()
#nft20 = ''.lowe 

values = defaultdict(int)

with open(file,'r') as file_r:
    reader = pd.read_csv(file_r)
    for row in reader.itertuples():
        address = row.to_address
        if address in platforms:
            values[platforms[address]] += 1

draw_pie('Comparing Platforms',values.values(),values.keys(),'platforms')