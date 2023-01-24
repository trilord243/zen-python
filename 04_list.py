""" numbers=[1,3,3,4,5,9,7,5]

numbers_2=[1,1,1,1,2,2,2,3,5,9,7,8,4,1,6,2,69,45,5689,5]
numbers_2=set(numbers_2)
numbers_2=list(numbers_2)


print(numbers_2)
numbers_3=[i for i in numbers_2 if i%2==0]


numbers_4=[i*2 for i in numbers_2 if i%2==0]



print(numbers_3)
print(numbers_4)
 numbers_v2=[element*2 for element  in numbers if element%2==0  ]
print(numbers_v2)





 """
 
 
 
numbers=[i for i in range(1,100) if i%2==0]
print(numbers)


numbers_2=[i for i in  range(1,100) if i%2!=0 ]
print(numbers_2)