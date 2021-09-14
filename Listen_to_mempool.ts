import { ethers } from "ethers";
const Web3 = require("web3");

const provider_selfhosted = new ethers.providers.WebSocketProvider(
  "ws://127.0.0.1:8646"
);
const web3 = new Web3("ws://127.0.0.1:8646");

web3.eth.net.getPeerCount().then(console.log);

const fs = require("fs");
const file = fs.createWriteStream("mempool_tran.json", { flags: "a" });

// eslint-disable-next-line
const subscription = web3.eth.subscribe("pendingTransactions", (err, res) => {
  if (err) console.error(err);
  //if (res) console.log(res);
});

subscription.on("data", (txHash) => {
  setTimeout(async () => {
    try {
      const txy = await web3.eth.getTransaction(txHash);
      if (txy && txy.from != null && typeof txy.from !== "undefined") {
        //console.log(JSON.stringify(txy) + ',');
        //file.write(JSON.stringify(txy) + ",");
        file.write(JSON.stringify(txy) + "," + "\n");
      }
    } catch (err) {
      console.error(err);
    }
  });
});
