import csv
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

transactions = list()
mempool = '/home/ruth/mempool_tx.json'
result = open("result_file.txt", "w")



file = r'/home/ruth/NFT-study/Ruth/Transactions/13160000_13199521/13160000_13199521.csv'

with open(file, 'r') as tx:
  reader = pd.read_csv(tx)
  for row in reader.itertuples():
    tx_hash = row.hash.lower()
    transactions.append(tx_hash)


with open(mempool,'r') as f:
  line = f.readline()
  line2 = line[:len(line)-2]

mempool_tx = list()
line3 = line2.split('},')
for i in line3:
  i = i.replace('null', 'None')
  data = i + "}"
  try:
    item = eval(data)
    mempool_tx.append(item['hash'].lower())
  except SyntaxError:
    pass
  except KeyError:
    pass

exlude = set(transactions)
new_list = [x for x in mempool_tx if x not in exlude] #transactions that didnt make it to blockchain

count_tx = len(transactions)
count_drop = len(new_list)
num_of_mem = len(mempool_tx)

drop_tx = (count_drop/num_of_mem) * 100

result.write("Dropped transactions" +"\n")
result.write("Total number of transactions: " + str(count_tx)+"\n")
result.write("Total number of drop transactions: " + str(count_drop)+ "\n")
result.write("Total number of mempool transactions: " + str(num_of_mem)+"\n")
result.write("Percentage of dropped transactions: " + str(drop_tx)+"%"+"\n")

result.close()
y = [num_of_mem-count_drop, count_drop]
mylabels = ["Transactions", "Dropped Transactions"]

plt.pie(y, labels = mylabels, autopct='%.2f')
plt.title('Dropped Transactions')
plt.legend()
plt.savefig('/home/ruth/NFT-study/Ruth/Plots/Dropped_tx.png')

