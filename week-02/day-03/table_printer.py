#Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ 'vodka': 1, 'needs_cooling': True },
	{ 'coffee_liqueur': 0, 'needs_cooling': True },
	{ 'fresh_cream': 1, 'needs_cooling': True },
	{ 'captain_morgan_rum': 2, 'needs_cooling': True },
	{ 'mint_leaves': 0, 'needs_cooling': False },
	{ 'sugar': 100, 'needs_cooling': False },
	{ 'lime juice': 10, 'needs_cooling': True },
	{ 'soda': 100, 'needs_cooling': True }
]
first_keys = []
for i in range(len(ingredients)):
    first_keys += [(list(ingredients[i].keys())[0])]
print(first_keys)
len_column_1 = len(max(first_keys, key=len)) + 1

minus='+'
for j in range(len_column_1):
    minus  += '-'

minus +='+'
for h in range(0,15):
    minus += '-'
minus +='+'
for h in range(0,10):
    minus += '-'
minus +='+'
print(minus) #1.vonal
header='| '
header +='Ingridients' 
for j in range(len_column_1-len('ingredients')-1):
    header +=" "
header+= '| Needs cooling | In stock | '
print(header)
print(minus) #2. vonal

i=0
for lines in ingredients:
    row='|'
    row +=first_keys[i]
    for j in range(len_column_1-len(first_keys[i])):
        row +=" "
    row +='| '
    if lines['needs_cooling']:
        row+='Yes'
    else:
        row+='No '
    for j in range(15-len('Yes')-1):
        row +=" "
    row +='|'        
   
    row += str((lines[first_keys[i]]))
    for j in range(10-len(str(lines[first_keys[i]]))-1):
        row +=" "
    row +=' |'

    i +=1
    print(row)
print(minus) #3.vonal