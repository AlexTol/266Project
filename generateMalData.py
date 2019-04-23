import random
expervals = []
payvals = []
for i in range(0,250):
    lexperience = random.randint(0,1)
    expervals.append(lexperience)
    hpay = random.randint(100000,500000)
    payvals.append(hpay)



for i in range(0,250):
    hexperience = random.randint(10,20)
    expervals.append(hexperience)
    lpay = random.randint(10000,33000)
    payvals.append(lpay)

with open('maliciousData.csv','w') as f:
        for i in range(0,500):
                f.write(str(expervals[i]) + ',' + str(payvals[i]) + '\n')