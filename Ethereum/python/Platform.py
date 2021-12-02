import pandas as pd
import csv
from collections import defaultdict
import datetime
import sys
csv.field_size_limit(sys.maxsize)

#from runner_tx import * 
#sys.path.append('/home/ruth/NFT-study/Ruth')
#from utils import *

platforms = {'0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'.lower():'OpenSea','0x60f80121c31a0d46b5279700f9df786054aa5ee5'.lower():'Rarible',
 '0xE052113bd7D7700d623414a0a4585BCaE754E9d5'.lower():'Niftyv Gateway','0x2fE9263BF105095e16167C093C4d28140e936E1b'.lower():'kiwiswap',
 '0x87d73E916D7057945c9BcD8cdd94e42A6F47f776'.lower():'nftx','0x88341d1a8F672D2780C8dC725902AAe72F143B0c'.lower():'nftfi',
 '0xD8E3FB3b08eBA982F2754988d70D57eDc0055ae6'.lower():'zora','0xba5bde662c17e2adff1075610382b9b691296350'.lower():'SuperRare',
 '0x3B3ee1931Dc30C1957379FAc9aba94D1C48a5405'.lower():'Foundation','0xb6ca7399b4f9ca56fc27cbff44f4d2e4eef1fc81'.lower():'NFT20'}

ether = lambda value: value / 1e18

START_BLOCK=11559999
END_BLOCK=13504400 
STEP_SIZE=2000000

nums = [defaultdict(int) for i in range(12)]
volume = [defaultdict(int) for i in range(12)]
unique_address = [defaultdict(set) for i in range(12)]

counter = 0
with open('/home/ruth/NFT-study/Ruth/Ethereum/Data/transactions.csv','r') as file_r:
    reader = csv.reader(file_r)
    #with open('ether-transactions.csv','w') as file_w:
     #   writer = csv.writer(file_w)
    for row in reader:
        if counter==0: 
            counter += 1
            continue
        address =str(row[6]).lower()
        month = datetime.datetime.fromtimestamp(int(row[11])).strftime("%m")
        temp = int(month)-1
        if address in platforms:
            nums[temp][platforms[address]] += 1
            volume[temp][platforms[address]] += ether(int(row[7]))
            unique_address[temp][platforms[address]].add(str(row[5]).lower())
            
        counter += 1
        if counter%100000==0:
            print(counter)


    with open('result.txt','w') as f:
        f.write("nums"+"\n")
        for i in range(len(nums)):
            f.write(str(i)+ " "+ str(nums[i])+"\n")

        f.write("volume"+"\n")
        for i in range(len(volume)):
            f.write(str(i) + " "+ str(volume[i])+"\n")

        f.write("unique_address"+"\n")
        for i in range(len(unique_address)):
            f.write(str(i) + " "+ str(unique_address[i])+"\n")
        
        


    size = []
    for i in volume:
        for key in i:
            i[key] = round(i[key],2)

     #reader = pd.read_csv(file_r)
        #for row in reader.itertuples():
         #   address = str(row.to_address).lower()
          #  if address in platforms:
           #     month = datetime.datetime.fromtimestamp(row.block_timestamp).strftime("%m")
            #    temp = int(month)-1
             #   nums[temp][platforms[address]] += 1
              #  volume[temp][platforms[address]] += ether(int(row.value))
               # address[temp][platforms[address]].add(str(row.from_address).lower())
    

    #draw_mult_bars(num,v1,v2,v3,x_label,y_label,x_ticks,names,title,file_name): 
    #draw_mult_bars('Volume of different platforms',values.keys(),values.values,'Platforms','Volume','platforms-volume')


