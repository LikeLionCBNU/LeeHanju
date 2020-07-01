numbers = range(100+1)

for n in numbers:
    if (n-3)%10 == 0 or (n-4)%10 == 0: pass
    else: print(n)

n = 0
while True:
    if n > 100: break
    if (n-3)%10 == 0 or (n-4)%10 == 0: pass
    else: print(n)
    n+=1
