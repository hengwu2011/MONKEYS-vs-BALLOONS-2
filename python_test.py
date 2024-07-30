"goal"

#produce a second list in which each dicts counter value is equal to the original lists counter value combined tih the previous items counter value
#ingredients: a second list, 2nd dicts counter value = og list value, + og previous value 
#translation: how to grab each counter value: how to get each obj in a list ---
import random as rd
dict_list = []
for n in range(20):
    dict_list.append({"counter":rd.random()})

add_list = []
