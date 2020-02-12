# Taking LS
Category: `FORENSICS`

Just take the Ls. Check out this zip file and I be the flag will remain hidden. 

https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8

## Write-up
透過題目下載一個壓縮檔，當要解壓縮時會發現有個檔案`The Flag.pdf`，

而且需要密碼

在終端機輸入ls看也還是只有看到這個pdf檔(注意前往資料夾看時因為有空白所以要輸入`cd The\ Flag`)

這時就要看看這資料夾裡藏了什麼，所以要輸入
```
ls -al
```

就會發現有個`.password`

讀取時會發現 : 
```
Nice Job!  The Password is "Im The Flag".
```

再去打開pdf檔案輸入`Im The Flag`

即可找到flag

Flag : `lag ABCTF{T3Rm1n4l_is_C00l}`
