my_list = [1, 2, 3, 4, 5]

# for loop 
# total = 0
# for i in my_list:
#     total= total+ i
# print (total)



#    # short cut 
# print(sum(my_list))

# range 
# for i in range(1, 13):
# #     print(i*12)
# shopping_cart = ['2KG RICE', 'Bread', 'Egg', 'bottle']
# for i in range(0, len(shopping_cart)):
#     print(shopping_cart[i])
# using a forloop for dictionary 

bio = {
    'name' : 'Motlokwe',
    'age' : 26,
    'job' : 'accountant',
    'location' : 'Johannesburg'
}

for key, value in bio.items():
    print(f'{key} =>{value}')
