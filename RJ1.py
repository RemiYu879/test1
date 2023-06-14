import sys
nums=[]

with open('test.txt',encoding='utf-8') as file:
    for line in file.readlines():
        try:
            num=int(line)
        except ValueError as e:
            
            continue
        nums.append(num)

    
    print(sum(nums))