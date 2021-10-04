import pandas as pd
import csv

file = r'/home/ruth/NFT-study/javascript-stuff/Ruth/13300000_13340000.csv'
result = 'address.txt'

#openSea_Contract = '0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'.lower()

with open(file,'r') as file_r:
    with open(result,'w') as file_w:
        reader = pd.read_csv(file_r)
        for row in reader.itertuples():
            #if row.to_address.lower() == openSea_Contract:
            tx = row.from_address.lower()
            file_w.write(str(tx) +"\n")
            #print(typeof(row.gasPrice))
         