import { ethers } from "ethers";
import { writeFileSync } from "fs";

const provider = new ethers.providers.WebSocketProvider(
  "http://127.0.0.1:8748"
);

const file = "NullAddress.txt"

provider.on("pending", (txHash) => {
  setTimeout(async function () {
  try{
      const txy = await provider.getTransaction(txHash);
      let unsigned_txy = undefined; 
      if (txy.from === '0x0000000000000000000000000000000000000000'){
        if (txy.type == 0) {
          unsigned_txy = {
            chainId: txy.chainId,
            data: txy.data,
            gasPrice: txy.gasPrice,
            gasLimit: txy.gasLimit,
            nonce: txy.nonce,
            to: txy.to,
            type: txy.type,
            value: txy.value,
          };
        } else if (txy.type == 2) {
          unsigned_txy = {
            chainId: txy.chainId,
            data: txy.data,
            gasPrice: txy.gasPrice,
            gasLimit: txy.gasLimit,
            maxFeePerGas: txy.maxFeePerGas,
            maxPriorityFeePerGas: txy.maxPriorityFeePerGas,
            nonce: txy.nonce,
            to: txy.to,
            type: txy.type,
            value: txy.value,
          };
        } else {
          return;
        }
        if (txy && txy.r && txy.s && txy.v){
          const expandedSig = {
            r: txy.r,
            s: txy.s,
            v: txy.v
          };
        
          const signature = ethers.utils.joinSignature(expandedSig);
          const raw = ethers.utils.serializeTransaction(unsigned_txy);
          const msgHash = ethers.utils.keccak256(raw); 
          const msgBytes = ethers.utils.arrayify(msgHash); 
          const recoveredAddress = ethers.utils.recoverAddress(msgBytes, signature);
          let ad = undefined;
          if (recoveredAddress === txy.from){
            ad = 'Same address';
          }
          else{
           ad ='Not same address';
          }
            
          writeFileSync(file ,"\n" + `TX HASH: ${txHash}`+ "\n" +`recovered address: ${recoveredAddress}`+"\n"+
          `Ethers address: ${txy.from}`+ "\n" + ad +"\n"+ JSON.stringify(txy) + "," + "\n",{
                encoding: "utf8",
                flag: "a+"});

          /*console.log("\n");
          console.log(`TX HASH: ${txHash}`);
          console.log(`recovered address: ${recoveredAddress}`);
          console.log(`Ethers address: ${txy.from}`);
          if (recoveredAddress === txy.from){
            console.log('Same address');
          }
          else{
            console.log('Not same address');
          }
          console.log(`Txy type: ${txy.type}`);
          console.log("\n");*/
        }
  }
     
  }catch (err) {
    console.error(err);
  }
  });
});

async function main() {
  console.log("Hello World");
  
}

main();