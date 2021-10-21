import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

dict_fun = defaultdict(int)
names = ['num', 'txns_hash', 'nonce', 'block_hash', 'block_number','transaction_index','from_address', 'to_address', 'value', 
'gas', 'gas_price', 'input', 'block_timestamp']

functions = {'Atomic Match':'0xab834bab', 'Cancel Order':'0xa8a41c70','Transfer': '0x','approveOrder':'0x79666868'}

with open('/home/ruth/NFT-study/Ruth/Csv_files/opensea_tx.csv', 'r') as file_r:
    reader = pd.read_csv(file_r,sep=',',usecols=names)
    input = reader['input']
    for item in input:
      fun = str(item)[:10]
      for name, num in functions.items():
        if num ==fun:
          dict_fun[name] += 1
    
    print(dict_fun.keys())
    print(dict_fun.values())

#plt.bar(dict_fun.keys(), dict_fun.values())

mylabels = dict_fun.keys()
plt.pie(dict_fun.values(), autopct='%.2f')
plt.legend(labels=mylabels,loc="center right", bbox_to_anchor=(1,1))
plt.title('Input OpenSea functions',loc='left')
plt.savefig('/home/ruth/NFT-study/Ruth/Plots/Input_funcOpenSea.png')



    



