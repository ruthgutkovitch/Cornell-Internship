import pandas as pd
import csv
from collections import defaultdict
import datetime
from runner_tx import * 
sys.path.append('/home/ruth/NFT-study/Ruth')
from utils import *

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
address = [defaultdict(set) for i in range(12)]

#files = ['transactions.csv'] #,'token_transfers.csv']
def compare_platforms(): 
    counter = 0
    with open('transactions.csv','r') as file_r:
        print("1")
        reader = pd.read_csv(file_r)
        print("2")
        for row in reader.itertuples():
            print("3")
            address = str(row.to_address).lower()
            if address in platforms:
                month = datetime.datetime.fromtimestamp(row.block_timestamp).strftime("%m")
                temp = int(month)-1
                nums[temp][platforms[address]] += 1
                volume[temp][platforms[address]] += ether(int(row.value))
                address[temp][platforms[address]].add(str(row.from_address).lower())

            with open('result.txt','a') as f:
                f.write(file + "\n" +str(nums)+"\n"+ str(volume)+"\n"+str(address)+"\n")


    size = []
    for i in volume:
        for key in i:
            i[key] = round(i[key],2)
    

    #draw_mult_bars(num,v1,v2,v3,x_label,y_label,x_ticks,names,title,file_name): 
    #draw_mult_bars('Volume of different platforms',values.keys(),values.values,'Platforms','Volume','platforms-volume')

if __name__ == "__main__":
    #get_blocks_and_transactions(START_BLOCK, END_BLOCK, STEP_SIZE)
    #get_token_transfers(START_BLOCK, END_BLOCK, STEP_SIZE)
    compare_platforms()

