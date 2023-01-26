items=[{
    
    "product_id":1,
    "product":"camisa",
    "price":100,

},{
    
    "product_id":2,
    "product":"pantalon",
    "price":200,

},{
    
    "product_id":3,
    "product":"zapatos",
    "price":50,

}
       ]




new_items=[items[i]["product"] for i in range(len(items))]

print( new_items )

def tax(items):
    items["tax"]=items["price"]*.19
    return items
    
    
new_items2=list(map(tax,items))

print(new_items2)