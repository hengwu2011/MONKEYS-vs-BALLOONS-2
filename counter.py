
#GOAL Make a list of 100 dictionaries each with a "counter" prop,
#that all have different even numbers as the value
#INGREDIENTS # a counter property, 100 dicts, a list
#TRANSLATION
list_random = [ {"counter": x*2} for x in range(100)]
print(list_random)