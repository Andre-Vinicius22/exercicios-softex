from time import time


import time

for contador in range(10, 0, -1):
    print(f'{contador} Segundos para o detonamento!')
    time.sleep(1)
else:
    print("BUUM!!")
