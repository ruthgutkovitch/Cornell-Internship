import os 
import glob
import pandas as pd
os.chdir("/home/ruth/NFT-study/Ruth/Tezos/Data1")

extension ='csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
combined_csv = combined_csv.to_csv("tezos_transactions_01.csv",index=False,encoding='utf-8-sig')

