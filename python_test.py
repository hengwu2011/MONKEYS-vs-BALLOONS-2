"goal"

#produce a second list in which each dicts counter value is equal to the original lists counter value combined tih the previous items counter value
#ingredients: a second list, 2nd dicts counter value = og list value, + og previous value 
#translation: how to grab each counter value: how to get each obj in a list ---
import random as rd
dict_list = []
for n in range(20):
    dict_list.append({"counter":rd.random()})

add_list = []
"""- invisible cities - italo calvino
  - invisible man - ralph ellison
  - little brother - cory doctorow
  - pride and prejudice - jane austen
  - cats cradle - kurt vonnebut
  - brave new world - aldous huxley
  - to kill a mockingbird - harper lee
  - of mice and men - john steinbeck
  - enchiridion - epictetus
  - the stranger - albert camus
  - siddartha - hermann hesse
  - don quixote - miguel de cervantes saavedra
  - the woman in the dunes - kobo abe 
  - cat in the hat - dr suess
  - yurtle the turtle - dr suess
  - on the shortness of life life is long if you know how to use it - seneca"""