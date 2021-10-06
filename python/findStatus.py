from web3 import Web3
import matplotlib.pyplot as plt
import pandas as pd

file = r'/home/ruth/NFT-study/javascript-stuff/Ruth/13300000_13340000.csv'
fail, success = 0, 0

#w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8646'))
w3 = Web3(Web3.HTTPProvider('http://localhost:8646'))
#try:
 # print(w3.isConnected())
#except Exception as e:
  #print(e)
  #print("error")
print(w3.eth.get_block('latest'))

with open(file, 'r') as r:
    reader = pd.read_csv(r)
    for row in reader.itertuples():
        hash = row.hash.lower()
        res = w3.eth.get_transaction_receipt(hash)
        if res[status]: success += 1
        else : fail += 1

names =["Failed tx", "Successful"]
plt.pie([fail, success], autopct='%.2f') 
plt.title("Failed transactions")
plt.legend(labels = names)
plt.savefig('/home/ruth/NFT-study/Ruth/Plots/failed_tx.png')
