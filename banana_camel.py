TotalBanana = int(input("no of bananas at start:"))
distance = int(input("Distance to be covered:"))
load_capacity = int(input("Max capacity to carry:"))

bananas_lost = 0
start = TotalBanana
for i in range(distance):
    while start>0:
        start = start - load_capacity
        if start == 1:
            bananas_lost -= 1
        bananas_lost = bananas_lost+2
        
    bananas_lost -= 1
    start = TotalBanana - bananas_lost
    
    if start == 0:
        break
print("Total bananas delivered:",start)
