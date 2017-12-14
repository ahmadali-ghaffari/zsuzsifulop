# Queue of festivalgoers at entry
# no. of alcohol units 
# no. of guns
# Create a security_check function that returns a list of festivalgoers who can enter the festival
# If guns are found, remove them and put them on the watchlist (only the names)
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

def guns():
    wachlist = []
    for i in range(len(queue)):
        if queue[i]['guns'] > 0:
            wachlist += [queue[i]['name']]
    print(wachlist)


def alcohol():
    security_alcohol_loot = 0
    for j in range(len(queue)):
        if queue[j]['alcohol'] > 0:
            security_alcohol_loot += queue[j]['alcohol']
            queue[j]['alcohol'] = 0
    print(security_alcohol_loot)


guns()
alcohol()