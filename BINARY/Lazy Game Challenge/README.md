# Lazy Game Challenge
Category: `BINARY`

I found an interesting game made by some guy named "John_123". 

It is some betting game. I made some small fixes to the game; see if you can still pwn this and steal $1000000 from me!

To get flag, pwn the server at: nc thekidofarcrania.com 10001

## Write-up
透過連結可以看到

![Figure1](https://github.com/Offliners/CTFlearn-writeup/blob/master/BINARY/Lazy%20Game%20Challenge/Figure1.PNG)

這是一個猜數字遊戲，而且要贏到1000000才能得到flag

看起來很難，但其實這有個bug

只要賭負數的錢

![Figure2](https://github.com/Offliners/CTFlearn-writeup/blob/master/BINARY/Lazy%20Game%20Challenge/Figure2.PNG)

這樣輸了的話就會`原有的錢 - 賭的錢`

負負得正，然後一直出大於10的數字穩輸(因為電腦只會出1~10而已)，就得到了flag~

![Figure3](https://github.com/Offliners/CTFlearn-writeup/blob/master/BINARY/Lazy%20Game%20Challenge/Figure3.PNG)

Flag : `CTFlearn{d9029a08c55b936cbc9a30_i_wish_real_betting_games_were_like_this!}`
