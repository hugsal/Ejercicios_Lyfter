time = int(input("Enter the time in seconds:"))
seconds_limit = 600
remaining_seconds = 0

if time == seconds_limit:
    print("Igual")
elif time < seconds_limit:
    remaining_seconds = seconds_limit - time
    print(remaining_seconds)
else:
    print("Mayor")
    