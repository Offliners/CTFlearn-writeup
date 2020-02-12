# Simple Programming
Category: `Programming`

Can you help me? I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. Please! Here is the file:

https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys

## Write-up
從題目連結可得到一個dat檔，

然後題目希望我們透過數出行數，且行必須符合0的個數是否為3的倍數與1是否為2的倍數

因此透過python
```python
count = 0
file = 'data.dat'

with open(file) as f:
    content = f.readlines()
    for line in content:
        zero = line.count('0')
        one = line.count('1')
        if(zero % 3 == 0) or (one % 2 == 0):
            count = count + 1

print('Number of lines : ', count)
```

得結果為6662，也就是flag

Flag : `6662`
