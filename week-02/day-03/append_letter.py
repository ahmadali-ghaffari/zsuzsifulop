# Add "a" to every string in far

far = ["kuty", "macsk", "kacs", "rók", "halacsk"]

def add (letter):
    for i in range(len(far)):
        far[i] += letter 
    print(far)
add('a')
