from web3 import Web3
import matplotlib.pyplot as plt
import pandas as pd
from utils import *
from runner_tx import *

START_BLOCK=13176499
END_BLOCK=13376499 
STEP_SIZE=200000

failed , successful = 0, 0 
get_blocks_and_transactions(START_BLOCK, END_BLOCK, STEP_SIZE)
get_column_from_transaction()
get_receipt()

with open('receipts.csv' , 'r') as file:
  reader = pd.read_csv(file)
  for row in reader.itertuples():
    status = row.status
    if status: successful+= 1
    else: failed += 1

values = [failed, successful]
names = ["Failed tx", "Successful tx"]

draw_pie('Failed tx',values,names,'failed' )

