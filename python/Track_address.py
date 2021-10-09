from collections import defaultdict
from collections import Counter
import pandas as pd
from utils import *

file = '/home/ruth/NFT-study/Ruth/transactions.csv'
dict_address = defaultdict(int)
contracts = ['Tether:USDT Stablecoin', 'OpenSea','Shiba Token', 'Uniswap V2: Router 2','Coinbase: Miscellaneous','USD Coin', 'other']



with open(file,'r') as f:
    reader = pd.read_csv(f)
    for row in reader.itertuples():
        address = row.to_address
        dict_address[address] += 1 

new_dict = dict(Counter(dict_address).most_common(6))
new_dict['other'] =sum(dict_address.values())-sum(new_dict.values())    

draw_donut('Most Common to Addresses',new_dict.values(),contracts,'To_address')

