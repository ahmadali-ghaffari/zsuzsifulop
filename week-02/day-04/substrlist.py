part_global= "ching" 
string_in_global = ["this", "is", "what", "I'm", "searching", "in"]

def string_modules(part, string_in):
    for item in string_in:
        if item.find(part) != -1:
            print(item.find(part))

string_modules(part_global, string_in_global)