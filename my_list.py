shopping_cart = ['2KG', 'bread', 'Egg', 'bottled water']


# updating a list 
# shopping_cart.append('5kg Rice* 5')
# using insert 
shopping_cart.insert(2, '5kg Rice*5')
shopping_cart.pop()

# pop with index 
shopping_cart.pop(0)

shopping_cart.reverse()
shopping_cart.sort(reverse=True)


print(shopping_cart)
