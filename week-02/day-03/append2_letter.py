# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters  # nopep8
# The string shouldf be a preverb
# The function appends every verb to the preverb and returns the list of the new verbs  # nopep8


verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"


def create_new_verbs(preverb):
    for i in range(len(verbs)):
        full_verb = preverb + verbs[i]
        print(full_verb)


create_new_verbs(preverb)
