import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import os

colors = ["pink","c","lightblue","lavender","lightcoral","wheat","beige"]

def autolabel(temp):
    for i in temp:
        h = i.get_height()
        plt.text(i.get_x()+i.get_width()/2,1.05*h,h,ha='center',va='bottom')

def draw_mult_bars(num,v1,v2,v3,x_label,y_label,x_ticks,names,title,file_name):
    ind = np.arange(num)
    w = 0.3

    r1 = plt.bar(ind,v1,width=w,align='center')
    autolabel(r1)
    r2 = plt.bar(ind+w,v2,width=w,align='center')
    autolabel(r2)
    r3 = plt.bar(ind+w*2,v3,width=w,align='center')
    autolabel(r3)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.legend((r1[0],r2[0],r3[0]),(names[0],names[0],names[0])) 
    plt.xticks(ind+w,labels=x_ticks)
    plt.title(title)
    plt.savefig(os.path.join(directory,'Plots/{}.png'.format(file_name)))



def draw_bar(title,keys,values,x_label,y_label,file_name,directory):
    bars = plt.bar(keys,values,color="c")
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x(),height,height)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig(os.path.join(directory,'Plots/{}.png'.format(file_name)))

def draw_donut(title,values,names,file_name):
    plt.pie(values, autopct='%.2f',colors=colors, rotatelabels =True,labels=names,startangle=150)
    circle = plt.Circle(xy=(0,0),radius=0.75,facecolor='white')
    plt.gca().add_artist(circle)
    plt.title(title)
    plt.savefig('/home/ruth/NFT-study/Ruth/Plots/{}.png'.format(file_name))

def draw_pie(title,values,names,file_name,directory):
    plt.pie(values, autopct='%.2f',colors=colors)
    plt.legend(labels=names)
    plt.title(title)
    plt.savefig(os.path.join(directory,'Plots/{}.png'.format(file_name)))

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
            reader = pd.read_csv(file_r,sep=',')
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
            if counter%1000000==0: num += 1
            with open('{}.txt'.format(num), 'a') as w:
                w.write(line)
            counter += 1

def get_data_from_tx(file):
    result = 'result.txt'
    with open(file,'r') as file_r:
        reader = pd.read_csv(file_r,sep=',')
        with open(result,'w') as file_w:
            for row in reader.itertuples():
                file_w.write(str(row.from_address)+"\n")

def get_data_about_address(file,data,address):
    result = 'result.txt'
    with open(file,'r') as file_r:
        reader = pd.read_csv(file_r,sep=',')
        with open(result,'w') as file_w:
            for row in reader.itertuples():
                if row.to_address == address:
                    result.write(row.data)

