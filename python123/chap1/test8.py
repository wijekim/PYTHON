num = int(input("정수 ="))

num1 = num % 10             
num10 = (num // 10) % 10    
num100 = (num // 100) % 10  
num1000 = (num // 1000) % 10 


sum = num1+num10+num100+num1000
print(sum)