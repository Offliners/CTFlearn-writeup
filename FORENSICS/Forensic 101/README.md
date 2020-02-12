# Forensic 101
Category: `FORENSICS`

Think the flag is somewhere in there. Would you help me find it? 

https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c

## Write-up
透過題目連結，可下載一張圖

![Figure](https://github.com/Offliners/CTFlearn-writeup/blob/master/FORENSICS/Forensic%20101/95f6edfb66ef42d774a5a34581f19052.jpg)

首先將圖片轉成文字檔看看，有沒有藏訊息

在Window上可用記事本開啟，再去搜尋flag

在linux可用
```
strings pic.jpg
```
再去尋找

果然flag就藏在其中

Flag : `flag{wow!_data_is_cool}`
