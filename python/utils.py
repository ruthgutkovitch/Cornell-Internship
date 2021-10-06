import matplotlib.pyplot as plt
import pandas as pd
import csv
import os

def draw_pie(title,values,names,file_name):
    plt.pie(values, autopct='%.2f')
    plt.legend(labels=names)
    plt.title(title)
    plt.savefig('/home/ruth/NFT-study/Ruth/Plots/{}.png'.format(file_name))

def draw_plot(x_values,y_values,x_label,y_label,title,file_name):
    plt.plot(x_values, y_values)
    plt.xlabel (x_label)
    plt.ylabel (y_label)
    plt.title(title)
    plt.xticks(x_values)
    plt.yticks(y_values)
    plt.savefig('/home/ruth/NFT-study/Ruth/Plots/{}.png'.format(file_name))
    

def csv_to_txt(file, name):
    with open(file,'r') as file_r:
        with open('result.txt','w') as file_w:
            reader = pd.read_csv(file_r)
            for row in reader.itertuples():
                tx = row.name
                file_w.write(str(tx) +"\n")

def opensea_tx(file):
    #head = ['num', 'txns_hash', 'nonce', 'block_hash', 'block_number', 'transaction_index','from_address', 'to_address', 'value', 'gas', 'gas_price', 'input', 'block_timestamp']
    
    head = ['hash','nonce','block_hash','block_number','transaction_index','from_address','to_address','value','gas',
    'gas_price','input','block_timestamp']
    openSea_Contract = '0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'.lower()

    with open('opensea.csv', 'w') as file_w:
        writer = csv.writer(file_w) 
        writer.writerow(head)
        with open(file, 'r') as file_r:
            reader = pd.read_csv(file_r,sep=',',usecols=names)
            for row in reader.itertuples():
                if row.to_address == openSea_Contract:
                    writer.writerow(row)
    
def split_large_file(file):
    curr = os.getcwd()
    path = os.path.join(curr,"New")
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)

    counter , num = 0, 0
    with open(file, 'r') as file:
        for line in file:
            if counter%100000==0: num += 1
            with open('{}.txt'.format(num), 'a') as w:
                w.write(line)
            counter += 1
