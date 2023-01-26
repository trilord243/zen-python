numbers=[1,2,3,4,5,6,7,8,9]

numbers_v2=[i*2 for i in numbers]
print(numbers_v2)


numbers_v3=list(map(lambda x:x*2,numbers))
print(numbers_v3)


numbers_2=[1,2,3,4,]

result=list(map(lambda x,y:x+y,numbers,numbers_2))

print(result)

