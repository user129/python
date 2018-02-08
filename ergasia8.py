import random
my_randoms = random.sample(range(-30,30), 30)
flag=False
print(my_randoms)
for l in range(30):
    for i in range( 0,30-2):
        for j in range(i+1, 30-1): 
            for k in range(j + 1, 30):
            
                if my_randoms[i] + my_randoms[j] + my_randoms[k]==0:
                    flag=True
                    print(my_randoms[i], my_randoms[j] , my_randoms[k])
if flag==False:
    print("den yparxei tetoios sundiasmos")
            
                    