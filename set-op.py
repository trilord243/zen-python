#Union
set_a={"col","mex","bol"}
set_b={"peru","bol"}


print(set_a & set_b )
set_c=set_a.intersection(set_b)
print(set_c)

#diferencia

set_c=set_a.difference(set_b)

print(set_c)
print(set_a-set_b)


#diferencia simetrica

set_c=set_a.symmetric_difference(set_b)
print(set_c)



