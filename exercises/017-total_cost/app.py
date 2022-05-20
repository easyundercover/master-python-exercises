#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
def total_cost(d,c,n):
    costo_dolares = n*d
    costo_centavos = n*c
    return costo_dolares, costo_centavos



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(60, 5, 10))
