import { ethers } from "ethers";
import { writeFileSync } from "fs";
import {createReadStream} from "fs";
import readline from "readline";

const mem ="pending_tx.txt";
const file_w = "NullAddress.txt";
const tx = "result.txt";

//define sets
var tx_set = new Set();
var mem_set = new Set();

//read tx 
var rd_tx =readline.createInterface({
    input: createReadStream(tx)
}); 
rd_tx.on('line',function(line){
    tx_set.add(line)
}) 

//read transactions from mempool
var rd_mem = readline.createInterface({
    input: createReadStream(mem)
});

rd_mem.on('line', function(line) {
    try{
        var txy = JSON.parse(line);
        if(tx_set.has(txy['hash'])==false){
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
                mem_set.add(recoveredAddress);
                /*if (txy['from']==='0x0000000000000000000000000000000000000000'){
                    writeFileSync(file_w ,"\n" + `TX HASH: ${txy['hash']}`+ "\n" +`recovered address: ${recoveredAddress}`+"\n"+
                    `Ethers address: ${txy['from']}`+ "\n" + ad +"\n"+ line + "," + "\n",{
                    encoding: "utf8",flag: "a+"});
                } */   
            }
        }
           
    }
    catch(err){
        console.error(err);
        return;
    }
    writeFileSync(file_w, `Number of sending addresses: ${mem_set.size}`+ "\n",{encoding: "utf8",flag: "a+"}); 
});

//console.log(from_address.size
