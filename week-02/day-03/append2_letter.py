# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "o"

#function add
def create_new_verbs(preverb):
    for i in range(len(verbs)):
        verbs[i] +=preverb
    print(verbs)
create_new_verbs(preverb)