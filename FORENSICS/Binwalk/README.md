# Binwalk
Category: `FORENSICS`

Here is a file with another file hidden inside it. Can you extract it? 

https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY

## Write-up
透過題目連結下載一張jpeg的圖片檔

![Figure](https://github.com/Offliners/CTFlearn-writeup/blob/master/FORENSICS/Binwalk/PurpleThing.jpeg)

由於題目直接提示我們binwalk，

binwalk是個可以看到圖片裡面藏有什麼資訊的軟體，所以二話不說直接下載binwalk

在終端機輸入 : 
```
sudo apt install binwalk
```

載好後輸入 : 
```
binwalk PurpleThing.jpeg
```

會看到
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 780 x 720, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, best compression
153493        0x25795         PNG image, 802 x 118, 8-bit/color RGBA, non-interlaced
156776        0x26468         Unix path: /www.w3.org/1999/02/22-rdf-syntax-ns#">
```



Flag : `flag{flag}`
