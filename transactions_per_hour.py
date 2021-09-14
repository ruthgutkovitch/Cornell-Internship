import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import seaborn as sns
sns.set_style('whitegrid')

ether = lambda value: value / 1e18

def main():
    transactions = pd.read_csv("/home/forsagedata/NFT-study/animetas/transactions_opensea.csv",
     sep=',', header=0, names=['num', 'txns_hash', 'nonce', 'block_hash', 'block_number', 'transaction_index',
      'from_address', 'to_address', 'value', 'gas', 'gas_price', 'input', 'block_timestamp'])

    transactions = transactions[transactions['value'].notna()]
    transactions['value'] = transactions['value'].astype(float)
    transactions['block_timestamp'] = transactions['block_timestamp'].astype(int)

    # convert block value to ether value
    transactions['value'] = ether(transactions['value'])
    x = range(24)
    y = [0]*24
    for i in range(len(transactions['block_timestamp'])):
        temp = datetime.datetime.fromtimestamp(transactions['block_timestamp'][i])
        date = temp.strftime("%Y-%m-%d")
        if date=='2021-07-31':
            hour = temp.strftime("%H")
            y[int(hour)] += transactions['value'][i]      
            #y[int(hour)] += 1 
    print(y)                
    plt.plot(x, y)
    plt.xlabel ('Hours')
    plt.ylabel ('Ether')
    #plt.ylabel('Number of OpenSea transactions')
    plt.title('Transactions per hour')
    plt.xticks(x)
    plt.yticks(range(0,2500,100))
    plt.grid(True)

    plt.savefig('/home/forsagedata/NFT-study/Ruth/Plots/OpenSea-transactions_per_hour.png')
    
    plt.show()

if __name__ == '__main__':
    main()