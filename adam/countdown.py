import time


n = 10
while True:
    print(n)
    n -= 1
    time.sleep(1)
    if n == 0:
        print('Blast off! 🚀')
        break

print('The rocket has launched')