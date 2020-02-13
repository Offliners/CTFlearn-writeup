# A CAPture of a Flag
Category: `FORENSICS`

This isn't what I had in mind, when I asked someone to capture a flag... can you help? You should check out WireShark. 

https://mega.nz/#!3WhAWKwR!1T9cw2srN2CeOQWeuCm0ZVXgwk-E2v-TrPsZ4HUQ_f4

## Write-up
這題應該是Easy等級中最難的了，

首先透過連結會載入一個flag(4)的檔案，

然後題目有提示說需要使用`Wireshark`

所以先下載 :
```
sudo apt install wireshark-qt
```

載好後開啟Wireshark，再把剛剛下載的檔案丟入，會看到 :

![Figure1]()

載來看一下他的http協定

![Figure2]()

有個神祕的msg訊息，拿去base64解密後就出現flag~

Flag : `flag{AFlagInPCAP}`
