# Hextroadinary
Category: `CRYPTO`

Meet ROXy, a coder obsessed with being exclusively the worlds best hacker. 

She specializes in short cryptic hard to decipher secret codes. 

The below hex values for example, she did something with them to generate a secret code, 

can you figure out what? Your answer should start with 0x.

0xc4115 0x4cf8

## Write-up
題目要我們把`0xc4115`和`0x4cf8`進行xor

那麼用python來求解
```python
print(hex(0xc4115 ^ 0x4cf8))
```

輸出即是flag~

Flag : `0xc0ded`
