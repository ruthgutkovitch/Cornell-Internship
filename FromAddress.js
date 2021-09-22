import { ethers } from "ethers";
import { writeFileSync } from "fs";
import {createReadStream} from "fs";
import readline from "readline";

const provider = new ethers.providers.WebSocketProvider(
    "http://127.0.0.1:8748"
  );

//Total number of drop transactions: 5256225
const file_r ="dropped_tx.txt";
const file_w = "NullAddress.txt";

var rd = readline.createInterface({
    input: createReadStream(file_r)
    //output: process.stdout,
    //console: false
});

var from_address= new Set();
rd.on('line', function(line) {
    try{
        var txy = JSON.parse(line);
    //console.log(obj)
        //if (txy['from']==='0x0000000000000000000000000000000000000000'){
            let unsigned_txy = undefined; 
            if (txy['type'] == 0) {
                unsigned_txy = {
                chainId: txy['chainId'],
                data: txy['data'],
                gasPrice: txy['gasPrice'],
                gasLimit: txy['gasLimit'],
                nonce: txy['nonce'],
                to: txy['to'],
                type: txy['type'],
                value: txy['value'],
            };
            } else if (txy['type'] == 2) {
                unsigned_txy = {
                chainId: txy['chainId'],
                data: txy['data'],
                gasPrice: txy['gasPrice'],
                gasLimit: txy['gasLimit'],
                maxFeePerGas: txy['maxFeePerGas'],
                maxPriorityFeePerGas: txy['maxPriorityFeePerGas'],
                nonce: txy['nonce'],
                to: txy['to'],
                type: txy['type'],
                value: txy['value'],
            };
            } else {
                return;
            }
            if (txy && txy['r'] && txy['s'] && txy['v']){
                const expandedSig = {
                r: txy['r'],
                s: txy['s'],
                v: txy['v']
                };
                const signature = ethers.utils.joinSignature(expandedSig);
                const raw = ethers.utils.serializeTransaction(unsigned_txy);
                const msgHash = ethers.utils.keccak256(raw); 
                const msgBytes = ethers.utils.arrayify(msgHash); 
                const recoveredAddress = ethers.utils.recoverAddress(msgBytes, signature);
                let ad = undefined;
                if (recoveredAddress === txy['from']){
                    ad = 'Same address';
                } else{
                    ad ='Not same address';
                }
                from_address.add(recoveredAddress);
                if (txy['from']==='0x0000000000000000000000000000000000000000'){
                    writeFileSync(file_w ,"\n" + `TX HASH: ${txy['hash']}`+ "\n" +`recovered address: ${recoveredAddress}`+"\n"+
                    `Ethers address: ${txy['from']}`+ "\n" + ad +"\n"+ line + "," + "\n",{
                    encoding: "utf8",flag: "a+"});
                }
            }
    }

    catch(err){
        //console.error(err);
        return;
    }
    
});

