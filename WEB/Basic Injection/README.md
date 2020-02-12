# Basic Injection
Category: `WEB`

See if you can leak the whole database. The flag is in there somwhere… https://web.ctflearn.com/web4/

## Write-up
透過題目連結，來到一個網站可輸入東西，

直覺反應是SQL injection

因此馬上輸入常見SQL injection語法
```
' OR '1' = '1
```

![Figure]()

果不其然，flag馬上出來~

Flag : `th4t_is_why_you_n33d_to_sanitiz3_inputs`
