set_countries={"Colombia","Francia","Alemania","Venezuela"}


print(set_countries)
print(len(set_countries))

print("Colombia" in set_countries)


numbers=[1,2,3,4]
numbers.append(2)

print(2 in numbers)
print(numbers)


#add

set_countries.add("Brasil")
print(set_countries)

#update

set_countries.update({"Argentina", "Ecuador"})
print(set_countries)


#delete
#set_countries.remove("Argentina")
set_countries.discard("Argentina")
print(set_countries)

set_countries.clear()
print(len(set_countries) )

print("")