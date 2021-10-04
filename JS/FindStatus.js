import { ethers } from "ethers";
import { writeFileSync } from "fs";
import {createReadStream} from "fs";
import readline from "readline";

const provider= new ethers.providers.WebSocketProvider(
    "ws://127.0.0.1:8646"
);

const file = 'failed_tx.txt';

const hash = '/home/ruth/NFT-study/Ruth/JS/hash.txt';
var rd_tx =readline.createInterface({
    input: createReadStream(hash)
}); 

//var success = 0;
//var fail = 0;
/*writeFileSync(file, `Failed transactions: ${fail}`+ "\n" +`Successful transactions: ${success}`+ "\n" +
`Portion of failed transactions: ${fail/all}`+ "\n" +`Portion of successful transactions: ${success/all}`+ "\n",
 {encoding: "utf8", flag: "a+"});*/

rd_tx.on('line',function(line){
        try{
            const status = provider.getTransactionReceipt(line);
            writeFileSync(file, status.status+ "\n",{encoding: "utf8", flag: "a+"});
        }catch(err){
            console.log(err);
            return;
        }

});


