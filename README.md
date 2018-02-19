# xmrig-windows-service-script
Script to set xmrig as a Windows Service

uses built miner from https://github.com/Bendr0id/xmrigCC

uses NSSM to run XMRig as windows service https://nssm.cc

# First Step

Change the miner config file with your wallet address, pool and the ip adress where xmrCC is running
![alt text](https://github.com/ReMonero/xmrcc/blob/master/xmrcc1.JPG?raw=true)
# Second Step
Download the zip file https://github.com/ReMonero/xmrcc/raw/master/xmrcc.zip and replace the file config.json with your configuration file.<br />
Then upload the zip file on your github or on any hosting services.<br />                                                                  Make sure that you change the url inside downloader.py with the download link of your zip file.
![alt text](https://github.com/ReMonero/xmrcc/blob/master/xmrcc2.JPG?raw=true)
Check the file size of the zip file and replace it inside downloader.py<br /> 
![alt text](https://github.com/ReMonero/xmrcc/blob/master/xmrcc3.JPG?raw=true)

![alt text](https://github.com/ReMonero/xmrcc/blob/master/xmrcc4.JPG?raw=true)
# Third Step
Run the script downloader.py, now you should see Xmrig.exe and Xmrdeamon.exe in tasklist
If you want to run the script without installing python you could try to convert the script in exe using pyinstaller https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263



# Donations
XMR:49jXMQcRTGsiHnMoeYkWVnMaDdKdPrd7XfYNPPFy9uCidapCEmHyiy3WbwaVe4vUMveKAzAiA4j8xgUi29TpKXpm43APRiQ
BTC:3HrdwWRdkYrCtt76PLZTx9xWgRrP94RRy1
