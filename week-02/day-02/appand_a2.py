# - Create a variable named `nimals`
#   with the following content: `["kuty", "macs", "cic"]`
# - Add all elements an `"a"` at the end

c = ["kuty", "macsk", "cic"]

def appendB(string):
    for i in range(len(c)):
        c[i] += string
    print(c)

appendB('a')
