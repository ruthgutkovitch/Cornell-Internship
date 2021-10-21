import csv
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

transactions = list()
mempool = '/home/ruth/mempool_tx.json'

file = r'/home/ruth/NFT-study/Ruth/13160000_13320190.csv'

with open(file, 'r') as tx:
  reader = pd.read_csv(tx)
  for row in reader.itertuples():
    tx_hash = row.hash.lower()
    transactions.append(tx_hash)

exlude = set(transactions)

with open(mempool,'r') as f:
  line = f.readline()
  line2 = line[:len(line)-2]

count_drop = 0 
#with open('dropped_tx.json','w') as file_w:
line3 = line2.split('},')
for i in line3:
  i = i.replace('null', 'None')+ "}"
  try:
    item = eval(i)
    if item['hash'].lower() not in exlude:
      count_drop += 1
        #for j in item:
            #if item[j]=='None': item[j]=='null'
            #if j=='value': item[j]='0x'+ item[j]
        #file_w.write(json.dumps(item)+"\n")
        #json.dumps(item, file_w, indent =2)

  except SyntaxError:
    pass
  except KeyError:
    pass

count_tx = len(transactions)
num_of_mem = len(line3)

drop_tx = (count_drop/num_of_mem) * 100

y = [num_of_mem-count_drop, count_drop]
mylabels = ["Transactions", "Dropped Transactions"]

plt.pie(y, labels = mylabels, autopct='%.2f')
plt.title('Dropped Transactions')
plt.legend()
plt.savefig('/home/ruth/NFT-study/Ruth/Plots/Dropped_tx_new.png')

