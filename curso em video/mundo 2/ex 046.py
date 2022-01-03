from time import sleep
print('hora dos fogos de artificios')
c=int(10)
for c in range(11,1,-1):
    sleep(1)
    print(c-1)
    c = c - 1
sleep(1)
print('BUM')