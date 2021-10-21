import * as solanaWeb3 from '@solana/web3.js';
import {createReadStream} from "fs";
import readline from "readline";

const connection = new solanaWeb3.Connection('https://api.mainnet-beta.solana.com');

connection.getBlocks(101000105,101000505).then(
    (account) => console.log(account)
);
var platforms = {'xxxxa1sKNGwFtw2kFn8XauW9xq8hBZ5kVtcSesTT9fW':'Solanium','METAewgxyPbgwsseH8T16a39CQ5VyVxZi9zXiDPY18m':'Metaplex',
'G7uYedVqFy97mzjygebnmmaMUVxWHFhNZotY6Zzsprvf':'CoreStarter','HsY8PNar8VExU335ZRYzg89fX7qa4upYu6vPMPFyCDdK':'Solible',
'SoLanartMarketpLace111111111111111111111111':'Solanart'
};

var file = '/home/ruth/NFT-study/Ruth/python/blocks.txt';
var read_block = readline.createInterface({
    input: createReadStream(file)
});

rd_mem.on('line', function(line) {
   line = line.replace(/(\n|[|])/gm,""); 
   var array = line.split(",");
   for (const elem of array){
        all_tx = connection.getBlock(elem).transactions;
        for (const i in all_tx){
           tx = i.transaction.message.accountKeys;

       }

   }

});