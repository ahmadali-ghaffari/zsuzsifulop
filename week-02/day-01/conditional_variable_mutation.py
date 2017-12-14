a = 24
b = 13
c = 123
d = 8
out = 0
out2 = ""
out3 = ""
credits = 100
is_bonus = False
time = 120

# if a is even increment out by one

if 24 % 2 == 0:
    out += 1
print(out)

# if b is between 10 and 20 set out2 to "Sweet!"
# if less than 10 set out2 to "More!",
# if more than 20 set out2 to "Less!"

if b > 10 and b < 20:
    print("Sweet!")
if b < 10:
    print("More")
if b > 20:
    print("Less")
print(out2)

# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits are smaller than 50,
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same

if credits > 49 and is_bonus == False:
    c -= 2
if credits < 50 and is_bonus == False:
    c -= 1
if is_bonus == True:
    c == c
print(c)

# if d is dividable by 4
# and time is not more than 200
# set out3 to "check"
# if time is more than 200
# set out3 to "Time out"
# otherwise set out3 to "Run Forest Run!"

if d % 4 == 0 and time > 200:
    out3 = "check"
if time > 200:
    out = "Time out"
else:
    out = "Run forest Run"
print(out3)
