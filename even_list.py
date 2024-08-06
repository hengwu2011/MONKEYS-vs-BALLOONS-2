#Goal Create a list in python that contains the first 100 even numbers after 38
# Ingrients need a list and print , for loop
# Translate list = even_fun = [], for x in range (40, 240)
even_list = []
starting_num = 38
for x in range(100):
    starting_num += 2 
    even_list.append(starting_num)


#print(even_list)
#Goal create a list in python of 25 random numbers ranging between [0,5]
#Ingridents need rd.random, need list, for loop
import random 
random_list = [random.random()*5 for x in range(25)]
print(random_list)