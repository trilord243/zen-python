increment=lambda x: x+1

hof=lambda x,func:x+func(x)

result=hof(1,increment)

print(result)
