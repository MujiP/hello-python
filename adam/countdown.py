import time

n = 10
while True:
    print(n)
    n -= 1
    time.sleep(0.5)
    if n == 0:
        print('Blast off! 🚀')
        break

for i in range(10, -1, -1):
    print(i)
    if i == 5:
        print('the engine has started 🔥')
    if i == 0:
        print('blast of 🚀 ') 
    time.sleep(1)
print('The rocket has launched')


n = 0

while True:
    print(n)
    n += 1
    time.sleep(1)

