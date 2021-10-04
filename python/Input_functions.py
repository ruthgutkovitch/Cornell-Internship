import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from collections import Counter

dict_fun = defaultdict(int)

names = ['hash','nonce','block_hash','block_number'	,'transaction_index','from_address',	'to_address',
	'value',	'gas',	'gas_price',	'input'	,'block_timestamp']

functions = {'0xab834bab':'Atomic Match','0xa8a41c70':'Cancel Order','0x':'Transfer', '0x7ff36ab5':'SwapExactETHForTokens','0x095ea7b3':'Approve','0xa9059cbb':'Transfer'}

with open('/home/ruth/NFT-study/Ruth/Transactions/12941301_12990000.csv', 'r') as file_r:
    reader = pd.read_csv(file_r,sep=',',usecols=names)
    input = reader['input']
    for item in input:
      fun = str(item)[:10]
      #for name, num in functions.items():
      if fun in functions:
        dict_fun[functions[fun]] += 1
      else:
        dict_fun[fun] += 1
    
    print(len(dict_fun))
    #print(dict_fun.values())

new_dict = dict(Counter(dict_fun).most_common(5))
new_dict_value = sum(new_dict.values())
new_dict['other'] = sum(dict_fun.values())-new_dict_value


mylabels = new_dict.keys()
plt.pie(new_dict.values(), autopct='%.2f')
plt.legend(labels=mylabels,loc="center right", bbox_to_anchor=(1,1))
plt.title('Input functions', loc='left')
plt.savefig('/home/ruth/NFT-study/Ruth/Plots/Input_func.png')


