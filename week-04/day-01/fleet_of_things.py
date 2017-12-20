# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

from fleet import Fleet
from thing import Thing

fleet = Fleet()

item_1 = Thing("Get milk")
print(item_1)
item_2 = Thing("Remove the obstacles")
print(item_2)
item_3 = Thing("Stand up")
item_3.complete()
print(item_3)
item_4 =Thing("Eat Lunch")
item_4.complete()
print(item_4)

print(fleet)