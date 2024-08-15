#Goal create a function in python which takes in two numbers a and b and returns a dictionary with two properties, 
# one being the sum of and 
# b and the other being the product of a and b
#Ingridents function, dict , variables, 
#translate function = def name(): dict = {}
def add_product(a,b):
    results = {
        "product":a*b,
        "add":a+b
    }
    return results
print(add_product(50,50))
  
   