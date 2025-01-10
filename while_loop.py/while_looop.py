# counter = 0

# while True:
#     counter += 1
#     if counter == 100:
#         continue
#     print(counter)
my_list = [1, 2, 3, 4, 5]

total = 0
while total <= 15:
    for i in my_list:
        total = total + i
    print(f'Total for this sequence is {total}')