""" dict={}

for i in range(1,5):
    dict[i]=i*2
    
    
print(dict)

dict_v2={ i:i*2 for i in range(1,5)  }

print(dict_v2) """
""" import random

paises=["col","mex","bol","pe"]


poblacion={}

for i in paises:
    poblacion[i]=random.randint(1,100)
    
print(poblacion)


poblacion_v2={i:"pais" for i in paises    }
print(poblacion_v2)


 """
 
 
""" names=["Nico","Sully", "Santy"]
ages=[12,56,98]

print(list(zip(names,ages)))


new_dict={name:age for (name,age) in zip(names,ages) }

print(new) """


numero={i:"numero" for i in range(1,10) }

print(numero)