passes = 0
failures = 0
counter = 0

for student in range(10):
    result = int(input("Enter result (1-pass, 2-fail): "))

    if result != 1 or 2:
        counter += 1
    else:
        if result == 1 or result == 2:
            passes += 1
        else:
            failures += 1


print('passed:', passes)
print('failed:', failures)
