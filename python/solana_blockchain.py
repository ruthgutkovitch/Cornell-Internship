from pysolana.api import * 
from collections import defaultdict
from collections import Counter
import datetime
from utils import *
import time
import re

platforms = {'xxxxa1sKNGwFtw2kFn8XauW9xq8hBZ5kVtcSesTT9fW':'Solanium','METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m':'Metaplex',
'G7uYedVqFy97mzjygebnmmaMUVxWHFhNZotY6Zzsprvf':'CoreStarter','HsY8PNar8VExU335ZRYzg89fX7qa4upYu6vPMPFyCDdK':'Solible',
'SoLanartMarketpLace111111111111111111111111':'Solanart'
}
addresses = defaultdict(int)
blocks = []
start_block = 101000105
end_block = 102432524

def getBlocks():
    counter = 0
    with open('blocks.txt', 'w') as file:
        for i in range(start_block,end_block,1000):
            nums = getConfirmedBlocks(i, i+999)
            file.write(str(nums)+"\n")
            #time.sleep(20)
            blocks.extend(nums)
            counter += 1
            print(counter)
            file.write(str(nums)+"\n")
    return blocks

def readBlocks():
    with open('blocks.txt', 'r') as file:
        for line in file:
            line = line.translate(str.maketrans("","",'[]\n'))
            new_list = line.split(",")
            blocks.extend(new_list)
    print(len(blocks))
    #print(blocks[0])
    #print(blocks[1])
    return blocks 


def getTransactions(blocks):
    counter = 0
    with open('platforms-solana.txt','w') as file: 
        for i in blocks:
            try:
                slot = getConfirmedBlock(int(i))
                counter += 1
                if counter%10==0:
                    time.sleep(20)
                    print(counter)
                    file.write(str(addresses)+"\n")
                    
                tx = slot['transactions']
                for j in tx:
                    accounts = j['transaction']['message']['accountKeys']
                    length = len(accounts)
                    if length>1:
                        for i in range(1,length):
                            if accounts[i] in platforms:
                                name = platforms[accounts[i]]
                                addresses[name] += 1
            
            except:
                pass
            
    draw_bar('Transactions number of different platforms',addresses.keys(),addresses.values(),'Platforms','Number','Solana-number')     
        

if __name__ == "__main__":
    #blocks = getBlocks()
    blocks = readBlocks()
    getTransactions(blocks)

