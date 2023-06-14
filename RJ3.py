import sys
num=[None]*1000
num1=[]
nums=[]



for i in range(1,1000,2):
    with open('sample\\sample\\kitamura_{}_kgu.txt'.format(f'{i:05}'),'r',encoding='utf-8') as file:
        num=file.read()
        
        try:
            num1=int(num)
        except ValueError as e:
            
            continue
        nums.append(num1)

print(sum(nums))