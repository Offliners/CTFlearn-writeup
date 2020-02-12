# Reversal of fortune
Category: `MISC`

Our team of agents have been tracking a hacker that sends cryptic messages to other hackers about what he's doing. We intercepted the below message he sent recently, can you figure out what it says? He mentions his hacker name in it, that's the code you need.

.nac uoy fi tIe$reveRpilF eldnah ym gnisu em egassem ,avaj yllacificeps ,gnidoc emos htiw pleh deen I ,deifitnedi tegrat txeN

## Write-up
看到題目的Reversal，然後把文字倒著看似乎有意思

於是使用python來把字串反轉

```python
encode = ".nac uoy fi tIe$reveRpilF eldnah ym gnisu em egassem ,avaj yllacificeps ,gnidoc emos htiw pleh deen I ,deifitnedi tegrat txeN"

decode = encode[::-1]

print(decode)
```

輸出內容為 : 
```
Next target identified, I need help with some coding, specifically java, message me using my handle FlipRever$eIt if you can.
```

即可看到flag

Flag : `FlipRever$eIt`
