# START
counter7: int = 0
num: int = int(input("Enter a number divisible by 7: "))
while True:
    if num % 7 == 0:
        counter7 += 1
        num: int = int(input("Enter a number divisible by 7: "))
    elif num % 11 == 0:
        break
    else:
        print(f"The number is not divisible by 7, you got {counter7} right numbers. ")
        break
# STOP
