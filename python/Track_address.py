import csv
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
from collections import Counter

dict_address = defaultdict(int)
transactions = list()

#functions = {'0x':'Transfer','0x095ea7b3':'Approve','0xa9059cbb':'0xa9059cbb','0x993e1c42':'WithdrawERC20For','0x379607f5':'0x379607f5'}

mempool = '/home/ruth/mempool_tx.json'
file = r'/home/ruth/NFT-study/Ruth/Transactions/13160000_13199521/13160000_13199521.csv'

with open(file, 'r') as tx:
  reader = pd.read_csv(tx)
  for row in reader.itertuples():
    tx_hash = row.hash.lower()
    transactions.append(tx_hash)

with open(mempool,'r') as f:
  line = f.readline()
  line2 = line[:len(line)-2]

dict_fun = defaultdict(int)
exlude = set(transactions)
counter = 0
line3 = line2.split('},')
for i in line3:
  i = i.replace('null', 'None')
  data = i + "}"
  try:
    item = eval(data)
    if item['hash'].lower() not in exlude:
      dict_address[item['from']] += 1 
      counter += 1
      if item['from'] == '0x0000000000000000000000000000000000000000':
        #fun = str(item['input'])[:10]
        #if fun in functions:
        dict_fun[item['to']] += 1
        #else:
         # dict_fun[fun] += 1
        #with open('tylerTest.txt', 'w') as file:
         # file.write(str(item))
        #break
  except SyntaxError:
    pass  
  except KeyError:
    pass


new_dict = dict(Counter(dict_fun).most_common(5))
new_dict['other'] =sum(dict_fun.values())-sum(new_dict.values())

with open('/home/ruth/NFT-study/Ruth/Txt_files/NullAdress.txt', 'w') as f:
  f.write('Number of destination addresses: '+ str(len(dict_fun))+ "\n")
  f.write('Number of transactions sent from Null Address: '+str(sum(dict_fun.values())))

plt.pie(new_dict.values(), autopct='%.2f')
plt.legend(labels=new_dict.keys(),loc="center right", bbox_to_anchor=(1,1))
plt.title('Address Null Destinations',loc='left')
plt.savefig('/home/ruth/NFT-study/Ruth/Plots/Addresses_0x0001.png')


