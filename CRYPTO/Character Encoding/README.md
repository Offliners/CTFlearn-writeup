# Character Encoding
Category: `CRYPTO`

In the computing industry, standards are established to facilitate information interchanges among American coders. Unfortunately, 

I've made communication a little bit more difficult. 

Can you figure this one out? 41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D

## Write-up
題目希望我們解碼這串數字，看起來應該是16進位，現在要轉成ASCII，

所以用python :
```python
hex_string = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D"
bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode("ASCII")
print(ascii_string)
```

轉完後就看到flag~


Flag : `ABCTF{45C11_15_U53FUL}`
