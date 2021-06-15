passes = 0
failures = 0
counter = 0

result = int(input("Enter result (1-pass, 2-fail): "))

while result != 1 or 2:
    result = int(input("Enter result (1-pass, 2-fail): "))
    counter += 1

    if result == 1:
        passes += 1
        print('passed:', passes)

    else:
        if result == 2:
            failures += 1
            print('failed:', failures)

        else:
            print("Enter Valid number")