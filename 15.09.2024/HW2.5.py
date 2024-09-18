# START
total_temp = 0
for i in range(1, 6):
    while True:
        temp: int = int(input(f"What is the temperature in city {i}?: "))
        if -50 <= temp <= 45:
            break
        else:
            print("The temperature is not in range, please try again: ")
    total_temp += temp
avg_temp = total_temp / 5
print(f"The average temperature is {avg_temp}")

# STOP
