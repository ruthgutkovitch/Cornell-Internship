import { ethers }  from "ethers";
import { writeFileSync } from "fs";
import {createReadStream} from "fs";
import readline from "readline";

const provider= new ethers.providers.WebSocketProvider(
    "ws://127.0.0.1:8646"
);

const file_w = "CompareAddress.txt";
const file_r = '/home/ruth/NFT-study/Ruth/JS/address.txt';
var rd_tx = readline.createInterface({
    input: createReadStream(file_r)
}); 

rd_tx.on('line',function(line){
        try{
            const code = provider.getCode(line);
            code.then(function(result){ ///need to change
                if (result=='0x'){
                    writeFileSync(file_w ,"human" +"\n",{encoding: "utf8",flag: "a+"});
                }else{
                    writeFileSync(file_w ,"smart contract" +"\n",{encoding: "utf8",flag: "a+"});
                   }
                })
            }catch(err){
                console.log(err);
                return;
            }
      
});

