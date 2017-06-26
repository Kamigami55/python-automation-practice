def collatz():
    global num
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1

while True:
    try:
        num = int(input())
    except ValueError:
        print("Please enter an integer")
        continue
    break

while num != 1:
    collatz()
    print(num)

