from pysolana.api import * 
from collections import defaultdict
from collections import Counter
import datetime
import time
import csv
import sys

#sys.path.append('/home/ruth/NFT-study/Ruth')
#from utils import *

platforms = {'xxxxa1sKNGwFtw2kFn8XauW9xq8hBZ5kVtcSesTT9fW':'Solanium','METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m':'Metaplex',
'G7uYedVqFy97mzjygebnmmaMUVxWHFhNZotY6Zzsprvf':'CoreStarter','HsY8PNar8VExU335ZRYzg89fX7qa4upYu6vPMPFyCDdK':'Solible',
'SoLanartMarketpLace111111111111111111111111':'Solanart','617jbWo616ggkDxvW1Le8pV38XLbVSyWY8ae6QUmGBAU':'SolSea',
'MEisE1HzehtrDpAAT8PnLHjpSSkRYakotTuJRPjTpo8':'Magic Eden'
}

ether = lambda value: value / 1e18

blocks = []
start_block = 89215482 
end_block = 104823222 

nums = [defaultdict(int) for i in range(12)]
volume = [defaultdict(int) for i in range(12)]
address = [defaultdict(set) for i in range(12)]

def getBlocks():
    counter = 0
    with open('blocks3.txt', 'w') as file:
        for i in range(start_block,end_block,1000):
            try:
                nums = getConfirmedBlocks(i, i+999)
                time.sleep(1)
                file.write(str(nums)+"\n")
                blocks.extend(nums)
                counter += 1
                print(counter)
                file.write(str(nums)+"\n")
            except:
                pass
    return blocks

def readBlocks():
    with open('blocks3.txt', 'r') as file:
        for line in file:
            line = line.translate(str.maketrans("","",'[]\n'))
            new_list = line.split(",")
            blocks.extend(new_list)
    print(len(blocks))
    return blocks 

def getTransactions(blocks):
    counter = 0

    with open('sol_transactions3.csv','w') as file_w:
        writer = csv.writer(file_w)
        headers = ['signature', 'block number','from address', 'to address', 'value','block timestamp']
        writer.writerow(headers)
        for i in blocks:
            try:
                slot = getConfirmedBlock(int(i))
                counter += 1
                if counter%10==0:
                    time.sleep(20)
                    print(counter)

                temp = datetime.datetime.fromtimestamp(slot['blockTime'])
                date = temp.strftime("%Y-%m-%d")
                month = int(temp.strftime("%m"))-1 
                block_num = int(i)
                tx = slot['transactions']

                for j in tx:
                    sig = j['transaction']['signatures'][0]
                    from_address = j['transaction']['message']['accountKeys'][0] #fee payer
                    value = j['meta']['postBalances'][0] - j['meta']['preBalances'][0]
                    j['transaction']['message']['accountKeys'].pop(0)
                    to_address = j['transaction']['message']['accountKeys']
                    writer.writerow([sig,block_num,from_address,to_address,value,date])

                    length = len(to_address)
                    for a in range(0,length):
                        if to_address[a] in platforms:
                            nums[month][platforms[to_address[a]]] += 1
                            volume[month][platforms[to_address[a]]] += ether(int(value))
                            address[month][platforms[to_address[a]]].add(str(from_address))
                
                with open('platforms3.txt','a') as f:
                    f.write(str(block_num)+ "\n"+ str(nums)+"\n"+ str(volume)+"\n"+str(address)+"\n")


            except:
                pass






if __name__ == "__main__":
    blocks = getBlocks()
    #blocks = readBlocks()
    getTransactions(blocks)

