# xmrig-windows-service-script
Script to set xmrig as a Windows Service

uses built miner from https://github.com/Bendr0id/xmrigCC

uses NSSM to run XMRig as windows service https://nssm.cc

# 1.First Step

Change the miner config file with your wallet address, pool and the ip adress where xmrCC is running
![alt text](https://github.com/ReMonero/xmrcc/blob/master/xmrcc1.JPG?raw=true)
# 2.Second Step
Download the zip file https://github.com/ReMonero/xmrcc/raw/master/xmrcc.zip and replace the file config.json with your configuration file.<br />
Then upload the zip file on your github or on any hosting services.<br />                                                                  Make sure that you change the url inside downloader.py with the download link of your zip file.
![alt text](https://github.com/ReMonero/xmrcc/blob/master/xmrcc2.JPG?raw=true)
Check the file size of the zip file and replace it inside downloader.py
![alt text](https://github.com/ReMonero/xmrcc/blob/master/xmrcc3.JPG?raw=true)
![alt text](https://github.com/ReMonero/xmrcc/blob/master/xmrcc4.JPG?raw=true)
