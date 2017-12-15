# Create a method that decrypts reversed-order.txt

file_name_global = "reversed-order.txt"

def reversed_order(file_name):
    try:
        read_in = open(file_name_global, 'r')
        text = read_in.readlines()
        print(text)
        string=""
        for i in range(len(text)-1, -1, -1):
            string += text[i]
        print(string)
    except IOError:
        print("Unable to write file: single-chars.txt")


reversed_order(file_name_global)
        