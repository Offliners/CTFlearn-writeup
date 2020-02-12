# Where Can My Robot Go?
Category: `MISC`

Where do robots find what pages are on a website?

Hint:

What does disallow tell a robot?

## Write-up

看到robot就想到使用`robots.txt`

於是在網址列輸入 :
```
https://ctflearn.com/robots.txt
```

就會看到
```
User-agent: *
Disallow: /70r3hnanldfspufdsoifnlds.html
```

但這還不是答案，還需要使用`curl`

於是打開終端機，輸入 : 
```
curl https://ctflearn.com/70r3hnanldfspufdsoifnlds.html
```

就可發現flag

Flag : `CTFlearn{r0b0ts_4r3_th3_futur3}`
