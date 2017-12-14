# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables
#print(current_time_in_seconds)

current_hours = 14
current_minutes = 34
current_seconds = 42

current_hour_in_seconds = current_hours * 60 * 60
current_minutes_in_seconds = current_minutes * 60
current_time_in_seconds = current_hour_in_seconds + current_minutes_in_seconds + current_seconds
seconds_in_a_day = 24 * 60 * 60
print(seconds_in_a_day-current_time_in_seconds)
