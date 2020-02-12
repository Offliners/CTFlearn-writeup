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
